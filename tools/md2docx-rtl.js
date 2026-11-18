// Build an Arabic (RTL) Word file from the house markdown format.
// Usage: node tools/md2docx-rtl.js input.md output.docx
//
// Supported markdown:
//   # / ## / ###         headings (H1 starts a new page when preceded by <!-- pagebreak -->)
//   ####                 small label line (e.g. HOOK (0–3 ث), [HEADLINE])
//   > text               note box;  > ON-SCREEN TEXT: text  -> on-screen text box
//   - item / 1. item     bullet and numbered lists
//   | a | b |            tables (optional <!-- cols: 30,70 --> line above sets column %)
//   **bold**, *italic*   inline (italic renders as a grey production note)
//   <!-- pagebreak -->   page break; everything before the first one is the cover page

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, BorderStyle, LevelFormat, Footer, PageNumber,
  HeadingLevel, VerticalAlign,
} = require("docx");

const [, , inPath, outPath] = process.argv;
if (!inPath || !outPath) {
  console.error("Usage: node md2docx-rtl.js input.md output.docx");
  process.exit(1);
}

const C = {
  green: "1F4D3A", gold: "9C7A3C", ivory: "F7F3EA", ink: "2B2B2B",
  gray: "6B6B6B", line: "D9CFBF", greenTint: "E9F0EB", white: "FFFFFF",
};
const FONT = "Arial";
const PAGE_W = 11906; // A4
const MARGIN = 1134; // 2 cm
const CONTENT_W = PAGE_W - 2 * MARGIN;
const SIZE = { body: 23, small: 20, table: 20, label: 18 };

const startsLatin = (s) => /^\[?\s*[A-Za-z]/.test(s.trim());

// Latin words/phrases become left-to-right runs; everything else stays right-to-left.
const LATIN_RE = /[A-Za-z](?:[A-Za-z0-9_\-./:@+=?&%#']*[A-Za-z0-9])?(?: [A-Za-z0-9](?:[A-Za-z0-9_\-./:@+=?&%#']*[A-Za-z0-9])?)*/g;

function run(text, base, rtl) {
  return new TextRun({
    text,
    font: FONT,
    size: base.size || SIZE.body,
    bold: !!base.bold,
    italics: !!base.italics,
    color: base.color || C.ink,
    rightToLeft: rtl,
  });
}

// In a left-to-right paragraph only Arabic words are right-to-left runs, so brackets
// and dashes around them keep their left-to-right order.
const ARABIC_RE = /[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]+(?:\s+[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]+)*/g;

function ltrRuns(text, base) {
  const out = [];
  let last = 0;
  let m;
  ARABIC_RE.lastIndex = 0;
  while ((m = ARABIC_RE.exec(text))) {
    if (m.index > last) out.push(run(text.slice(last, m.index), base, false));
    out.push(run(m[0], base, true));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(run(text.slice(last), base, false));
  return out;
}

function scriptRuns(text, base) {
  if (base.ltr) return ltrRuns(text, base);
  const out = [];
  let last = 0;
  let m;
  LATIN_RE.lastIndex = 0;
  while ((m = LATIN_RE.exec(text))) {
    if (m.index > last) out.push(run(text.slice(last, m.index), base, true));
    out.push(run(m[0], base, false));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(run(text.slice(last), base, true));
  return out;
}

function inline(text, base = {}) {
  const runs = [];
  const re = /\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let last = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > last) runs.push(...scriptRuns(text.slice(last, m.index), base));
    if (m[1] !== undefined) runs.push(...scriptRuns(m[1], { ...base, bold: true }));
    else runs.push(...scriptRuns(m[2], { ...base, italics: true, color: C.gray }));
    last = m.index + m[0].length;
  }
  if (last < text.length) runs.push(...scriptRuns(text.slice(last), base));
  return runs;
}

function para(text, o = {}) {
  const ltr = o.ltr === undefined ? false : o.ltr;
  return new Paragraph({
    bidirectional: !ltr,
    alignment: o.align !== undefined ? o.align : ltr ? AlignmentType.RIGHT : undefined,
    heading: o.heading,
    keepNext: !!o.keepNext,
    pageBreakBefore: !!o.pageBreakBefore,
    numbering: o.numbering,
    border: o.border,
    spacing: { before: o.before || 0, after: o.after === undefined ? 120 : o.after, line: o.line || 300 },
    children: inline(text, { ...(o.run || {}), ltr }),
  });
}

const thin = (color) => ({ style: BorderStyle.SINGLE, size: 4, color });
const boxBorders = (color) => ({ top: thin(color), bottom: thin(color), left: thin(color), right: thin(color) });

function box(paragraphs, fill, borderColor) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    visuallyRightToLeft: true,
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill, color: "auto" },
        borders: boxBorders(borderColor),
        margins: { top: 100, bottom: 100, left: 180, right: 180 },
        children: paragraphs,
      })],
    })],
  });
}

function spacer(after = 120) {
  return new Paragraph({ bidirectional: true, spacing: { before: 0, after, line: 240 }, children: [] });
}

function callout(text) {
  const onScreen = text.match(/^ON-SCREEN TEXT:\s*(.*)$/);
  if (onScreen) {
    return [
      box([
        para("ON-SCREEN TEXT", { ltr: true, after: 40, run: { size: 16, bold: true, color: C.gold } }),
        para(onScreen[1], { after: 0, run: { bold: true, color: C.green } }),
      ], C.greenTint, "B7CBBE"),
      spacer(),
    ];
  }
  return [box([para(text, { after: 0, run: { size: SIZE.small, color: C.ink } })], C.ivory, C.line), spacer()];
}

function table(rows, colsPct) {
  const n = rows[0].length;
  const pct = colsPct && colsPct.length === n ? colsPct : Array(n).fill(100 / n);
  const total = pct.reduce((a, b) => a + b, 0);
  const widths = pct.map((p) => Math.round((p / total) * CONTENT_W));
  widths[n - 1] = CONTENT_W - widths.slice(0, n - 1).reduce((a, b) => a + b, 0);
  const keepTogether = rows.length <= 12; // short tables stay on one page
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    visuallyRightToLeft: true,
    rows: rows.map((cells, r) => new TableRow({
      tableHeader: r === 0,
      cantSplit: true,
      children: cells.map((cell, c) => new TableCell({
        width: { size: widths[c], type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        shading: { type: ShadingType.CLEAR, color: "auto", fill: r === 0 ? C.green : r % 2 === 0 ? C.ivory : C.white },
        borders: boxBorders(C.line),
        margins: { top: 70, bottom: 70, left: 110, right: 110 },
        children: [para(cell, {
          ltr: /[A-Za-z]/.test(cell) && !/[؀-ۿ]/.test(cell),
          keepNext: keepTogether && r < rows.length - 1,
          after: 0,
          line: 276,
          run: r === 0 ? { size: SIZE.table, bold: true, color: C.white } : { size: SIZE.table },
        })],
      })),
    })),
  });
}

// ---------- parse ----------
const lines = fs.readFileSync(inPath, "utf8").replace(/\r/g, "").split("\n");
const cover = [];
const body = [];
let inCover = true;
let pendingBreak = false;
let nextCols = null;
let listInstance = 0;

const out = () => (inCover ? cover : body);
function takeBreak() {
  const b = pendingBreak;
  pendingBreak = false;
  return b;
}

for (let i = 0; i < lines.length; i++) {
  const t = lines[i].trim();
  if (!t) continue;

  if (/^<!--\s*pagebreak\s*-->$/.test(t)) {
    inCover = false;
    pendingBreak = true;
    continue;
  }
  const cols = t.match(/^<!--\s*cols:\s*([\d.,\s]+)-->$/);
  if (cols) {
    nextCols = cols[1].split(",").map((x) => parseFloat(x));
    continue;
  }

  if (inCover) {
    if (t.startsWith("# ")) {
      cover.push(para(t.slice(2), { align: AlignmentType.CENTER, before: 2600, after: 240, run: { size: 72, bold: true, color: C.green } }));
    } else if (cover.length === 1) {
      cover.push(para(t, {
        align: AlignmentType.CENTER, after: 720,
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.gold, space: 18 } },
        run: { size: 32, color: C.gold },
      }));
    } else {
      cover.push(para(t, { align: AlignmentType.CENTER, after: 200, run: { size: 24, color: cover.length === 2 ? C.ink : C.gray, bold: cover.length === 2 } }));
    }
    continue;
  }

  if (t.startsWith("|")) {
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith("|")) {
      const cells = lines[i].trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
      if (!cells.every((c) => /^:?-{2,}:?$/.test(c))) rows.push(cells);
      i++;
    }
    i--;
    body.push(table(rows, nextCols));
    body.push(spacer(160));
    nextCols = null;
    continue;
  }

  const h = t.match(/^(#{1,4})\s+(.*)$/);
  if (h) {
    const level = h[1].length;
    const text = h[2];
    const ltr = startsLatin(text);
    if (level === 1) {
      body.push(para(text, {
        heading: HeadingLevel.HEADING_1, pageBreakBefore: takeBreak(), keepNext: true, ltr, before: 0, after: 240,
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.gold, space: 6 } },
        run: { size: 36, bold: true, color: C.green },
      }));
    } else if (level === 2) {
      body.push(para(text, { heading: HeadingLevel.HEADING_2, keepNext: true, ltr, before: 300, after: 120, run: { size: 29, bold: true, color: C.green } }));
    } else if (level === 3) {
      body.push(para(text, { heading: HeadingLevel.HEADING_3, keepNext: true, ltr, before: 260, after: 100, run: { size: 25, bold: true, color: C.gold } }));
    } else {
      body.push(para(text, { keepNext: true, ltr, before: 180, after: 50, run: { size: SIZE.label, bold: true, color: C.gold } }));
    }
    continue;
  }

  if (t.startsWith(">")) {
    body.push(...callout(t.replace(/^>\s?/, "")));
    continue;
  }

  if (/^- /.test(t)) {
    while (i < lines.length && /^- /.test(lines[i].trim())) {
      body.push(para(lines[i].trim().slice(2), { numbering: { reference: "bullets", level: 0 }, after: 80 }));
      i++;
    }
    i--;
    body.push(spacer(60));
    continue;
  }

  if (/^\d+\.\s/.test(t)) {
    listInstance++;
    while (i < lines.length && /^\d+\.\s/.test(lines[i].trim())) {
      body.push(para(lines[i].trim().replace(/^\d+\.\s+/, ""), {
        numbering: { reference: "numbers", level: 0, instance: listInstance }, after: 80,
      }));
      i++;
    }
    i--;
    body.push(spacer(60));
    continue;
  }

  if (/^\*\*[^*]+\*\*$/.test(t)) {
    body.push(para(t.slice(2, -2), { keepNext: true, before: 160, after: 40, run: { bold: true, color: C.green } }));
    continue;
  }
  if (/^\*[^*]+\*$/.test(t)) {
    body.push(para(t, { after: 100, run: { size: SIZE.small } }));
    continue;
  }

  body.push(para(t, { pageBreakBefore: takeBreak() }));
}

// ---------- document ----------
const headingStyle = (size, color) => ({
  run: { font: FONT, size, bold: true, color },
  paragraph: { spacing: { before: 240, after: 120 }, keepNext: true },
});

const doc = new Document({
  creator: "Go Online",
  title: "أثر يبقى — ملف التنفيذ",
  styles: {
    default: {
      document: { run: { font: FONT, size: SIZE.body, color: C.ink } },
      heading1: headingStyle(36, C.green),
      heading2: headingStyle(29, C.green),
      heading3: headingStyle(25, C.gold),
    },
  },
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 520, hanging: 300 } }, run: { color: C.gold } },
        }],
      },
      {
        reference: "numbers",
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 520, hanging: 360 } }, run: { bold: true, color: C.green } },
        }],
      },
    ],
  },
  sections: [{
    properties: {
      titlePage: true,
      page: { margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } },
    },
    footers: {
      first: new Footer({ children: [] }),
      default: new Footer({
        children: [new Paragraph({
          bidirectional: true,
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "أثر يبقى · ملف التنفيذ · ", font: FONT, size: 16, color: C.gray, rightToLeft: true }),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: C.gray }),
          ],
        })],
      }),
    },
    children: [...cover, ...body],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`Wrote ${outPath}`);
});
