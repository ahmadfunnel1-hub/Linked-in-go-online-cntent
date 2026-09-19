/*!
 * Round-trip verification for qr-encoder.js. No dependencies -- `node test/verify.js`.
 *
 * Every symbol is decoded back through qr-decoder.js, which recovers the format
 * information from the symbol and checks all Reed-Solomon syndromes. A symbol
 * that passes is one a real scanner reads correctly.
 */
const { encodeQR, toSVG, minPrintSizeMM } = require('../qr-encoder.js');
const { decode } = require('../qr-decoder.js');

let pass = 0, fail = 0;
const failures = [];
const check = (name, fn) => {
  try { fn(); pass++; }
  catch (e) { fail++; failures.push(`${name}: ${e.message}`); }
};
const assert = (cond, msg) => { if (!cond) throw new Error(msg); };

const roundTrip = (text, ec) => check(`roundtrip ${ec} len=${text.length}`, () => {
  const q = encodeQR(text, ec);
  const d = decode(q.modules);
  assert(d.text === text, `payload mismatch (got ${JSON.stringify(d.text.slice(0, 40))})`);
  assert(d.ecLevel === ec, `ecc mismatch: ${d.ecLevel} != ${ec}`);
  assert(d.version === q.version, `version mismatch: ${d.version} != ${q.version}`);
  assert(d.mask === q.mask, `mask mismatch: ${d.mask} != ${q.mask}`);
});

// deterministic pseudo-random payloads across the whole version range
const CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&()*+,;=%";
let seed = 12345;
const rnd = () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; };

const LENGTHS = [1, 2, 3, 7, 11, 14, 17, 20, 26, 32, 40, 53, 64, 78, 90, 106, 122, 150, 200,
                 271, 350, 440, 550, 700, 900, 1100, 1273, 1500, 1800, 2100, 2300];
const versions = new Set();
for (const len of LENGTHS) {
  let s = ''; for (let i = 0; i < len; i++) s += CHARS[Math.floor(rnd() * CHARS.length)];
  for (const ec of ['L', 'M', 'Q', 'H']) {
    let q; try { q = encodeQR(s, ec); } catch { continue; }  // exceeds capacity at this level
    versions.add(q.version);
    roundTrip(s, ec);
  }
}

// shapes this repo actually prints
for (const url of [
  'https://go.example.com/m',
  'https://go.example.com/menu?utm_source=qr&utm_medium=print&utm_campaign=table_tent',
  'https://qr.mobi/f4c17dea',
  'مرحبا بكم',                       // UTF-8 byte mode
  'https://go.example.com/' + 'x'.repeat(400),
]) for (const ec of ['L', 'M', 'Q', 'H']) {
  try { encodeQR(url, ec); } catch { continue; }
  roundTrip(url, ec);
}

check('SVG keeps a 4-module quiet zone on every side', () => {
  const q = encodeQR('https://go.example.com/m', 'Q');
  const sizeMM = 40, quietZone = 4;
  const svg = toSVG(q, { sizeMM, quietZone });
  const unit = sizeMM / q.size;
  const tol = 1e-3;                       // SVG coordinates are rounded to 4dp
  const rects = [...svg.matchAll(/<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"/g)]
    .map(m => m.slice(1).map(Number));
  assert(rects.length > 0, 'no module rects emitted');
  const edge = unit * quietZone;
  const far = edge + sizeMM;
  for (const [x, y, w, h] of rects) {
    assert(x >= edge - tol && y >= edge - tol, 'module crosses the top/left quiet zone');
    assert(x + w <= far + tol && y + h <= far + tol, 'module crosses the bottom/right quiet zone');
  }
  const viewBox = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
  assert(Math.abs(Number(viewBox[1]) - (sizeMM + 2 * edge)) < tol, 'canvas width excludes the quiet zone');
});

check('ECC level raises symbol version for same payload', () => {
  const s = 'https://go.example.com/menu';
  assert(encodeQR(s, 'H').version >= encodeQR(s, 'L').version, 'H should need >= L');
});

check('oversized payload is rejected, not silently truncated', () => {
  let threw = false;
  try { encodeQR('x'.repeat(4000), 'H'); } catch { threw = true; }
  assert(threw, 'expected a capacity error');
});

check('print size rule of thumb', () => {
  const q = encodeQR('https://go.example.com/m', 'Q');
  assert(Math.abs(minPrintSizeMM(q, 1000) - 100) < 1e-9, 'expected 100mm at 1m');
});

console.log(`versions exercised: ${[...versions].sort((a, b) => a - b).join(',')}`);
console.log(`\n${pass} passed, ${fail} failed`);
if (fail) { console.log('\n' + failures.join('\n')); process.exit(1); }
