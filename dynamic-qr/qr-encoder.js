/*!
 * qr-encoder.js -- dependency-free QR Code encoder (byte mode, versions 1-40, ECC L/M/Q/H).
 * Implements ISO/IEC 18004:2015. Runs identically in Node and the browser.
 *
 * Verified by test/verify.js:
 *   - every symbol decodes back to its input with all Reed-Solomon syndromes zero
 *   - matrices are byte-identical to the `segno` reference library across
 *     versions 1-39 and all four ECC levels
 *
 * Spec note: ISO 18004 7.4.10 adds padding bits only when the bit stream does
 * not already end on a codeword boundary. segno appends a whole zero codeword
 * even when it does; `padCompat` reproduces that quirk for the cross-check.
 * Both forms scan identically -- the trailing bytes are padding either way.
 */
/* Minimal, spec-complete QR encoder (byte mode, versions 1-40, ECC L/M/Q/H).
   TABLES placeholder is replaced with the segno-derived spec tables at build time. */
const T = {"ecc":{"1":{"L":[[1,26,19]],"M":[[1,26,16]],"Q":[[1,26,13]],"H":[[1,26,9]]},"2":{"L":[[1,44,34]],"M":[[1,44,28]],"Q":[[1,44,22]],"H":[[1,44,16]]},"3":{"L":[[1,70,55]],"M":[[1,70,44]],"Q":[[2,35,17]],"H":[[2,35,13]]},"4":{"L":[[1,100,80]],"M":[[2,50,32]],"Q":[[2,50,24]],"H":[[4,25,9]]},"5":{"L":[[1,134,108]],"M":[[2,67,43]],"Q":[[2,33,15],[2,34,16]],"H":[[2,33,11],[2,34,12]]},"6":{"L":[[2,86,68]],"M":[[4,43,27]],"Q":[[4,43,19]],"H":[[4,43,15]]},"7":{"L":[[2,98,78]],"M":[[4,49,31]],"Q":[[2,32,14],[4,33,15]],"H":[[4,39,13],[1,40,14]]},"8":{"L":[[2,121,97]],"M":[[2,60,38],[2,61,39]],"Q":[[4,40,18],[2,41,19]],"H":[[4,40,14],[2,41,15]]},"9":{"L":[[2,146,116]],"M":[[3,58,36],[2,59,37]],"Q":[[4,36,16],[4,37,17]],"H":[[4,36,12],[4,37,13]]},"10":{"L":[[2,86,68],[2,87,69]],"M":[[4,69,43],[1,70,44]],"Q":[[6,43,19],[2,44,20]],"H":[[6,43,15],[2,44,16]]},"11":{"L":[[4,101,81]],"M":[[1,80,50],[4,81,51]],"Q":[[4,50,22],[4,51,23]],"H":[[3,36,12],[8,37,13]]},"12":{"L":[[2,116,92],[2,117,93]],"M":[[6,58,36],[2,59,37]],"Q":[[4,46,20],[6,47,21]],"H":[[7,42,14],[4,43,15]]},"13":{"L":[[4,133,107]],"M":[[8,59,37],[1,60,38]],"Q":[[8,44,20],[4,45,21]],"H":[[12,33,11],[4,34,12]]},"14":{"L":[[3,145,115],[1,146,116]],"M":[[4,64,40],[5,65,41]],"Q":[[11,36,16],[5,37,17]],"H":[[11,36,12],[5,37,13]]},"15":{"L":[[5,109,87],[1,110,88]],"M":[[5,65,41],[5,66,42]],"Q":[[5,54,24],[7,55,25]],"H":[[11,36,12],[7,37,13]]},"16":{"L":[[5,122,98],[1,123,99]],"M":[[7,73,45],[3,74,46]],"Q":[[15,43,19],[2,44,20]],"H":[[3,45,15],[13,46,16]]},"17":{"L":[[1,135,107],[5,136,108]],"M":[[10,74,46],[1,75,47]],"Q":[[1,50,22],[15,51,23]],"H":[[2,42,14],[17,43,15]]},"18":{"L":[[5,150,120],[1,151,121]],"M":[[9,69,43],[4,70,44]],"Q":[[17,50,22],[1,51,23]],"H":[[2,42,14],[19,43,15]]},"19":{"L":[[3,141,113],[4,142,114]],"M":[[3,70,44],[11,71,45]],"Q":[[17,47,21],[4,48,22]],"H":[[9,39,13],[16,40,14]]},"20":{"L":[[3,135,107],[5,136,108]],"M":[[3,67,41],[13,68,42]],"Q":[[15,54,24],[5,55,25]],"H":[[15,43,15],[10,44,16]]},"21":{"L":[[4,144,116],[4,145,117]],"M":[[17,68,42]],"Q":[[17,50,22],[6,51,23]],"H":[[19,46,16],[6,47,17]]},"22":{"L":[[2,139,111],[7,140,112]],"M":[[17,74,46]],"Q":[[7,54,24],[16,55,25]],"H":[[34,37,13]]},"23":{"L":[[4,151,121],[5,152,122]],"M":[[4,75,47],[14,76,48]],"Q":[[11,54,24],[14,55,25]],"H":[[16,45,15],[14,46,16]]},"24":{"L":[[6,147,117],[4,148,118]],"M":[[6,73,45],[14,74,46]],"Q":[[11,54,24],[16,55,25]],"H":[[30,46,16],[2,47,17]]},"25":{"L":[[8,132,106],[4,133,107]],"M":[[8,75,47],[13,76,48]],"Q":[[7,54,24],[22,55,25]],"H":[[22,45,15],[13,46,16]]},"26":{"L":[[10,142,114],[2,143,115]],"M":[[19,74,46],[4,75,47]],"Q":[[28,50,22],[6,51,23]],"H":[[33,46,16],[4,47,17]]},"27":{"L":[[8,152,122],[4,153,123]],"M":[[22,73,45],[3,74,46]],"Q":[[8,53,23],[26,54,24]],"H":[[12,45,15],[28,46,16]]},"28":{"L":[[3,147,117],[10,148,118]],"M":[[3,73,45],[23,74,46]],"Q":[[4,54,24],[31,55,25]],"H":[[11,45,15],[31,46,16]]},"29":{"L":[[7,146,116],[7,147,117]],"M":[[21,73,45],[7,74,46]],"Q":[[1,53,23],[37,54,24]],"H":[[19,45,15],[26,46,16]]},"30":{"L":[[5,145,115],[10,146,116]],"M":[[19,75,47],[10,76,48]],"Q":[[15,54,24],[25,55,25]],"H":[[23,45,15],[25,46,16]]},"31":{"L":[[13,145,115],[3,146,116]],"M":[[2,74,46],[29,75,47]],"Q":[[42,54,24],[1,55,25]],"H":[[23,45,15],[28,46,16]]},"32":{"L":[[17,145,115]],"M":[[10,74,46],[23,75,47]],"Q":[[10,54,24],[35,55,25]],"H":[[19,45,15],[35,46,16]]},"33":{"L":[[17,145,115],[1,146,116]],"M":[[14,74,46],[21,75,47]],"Q":[[29,54,24],[19,55,25]],"H":[[11,45,15],[46,46,16]]},"34":{"L":[[13,145,115],[6,146,116]],"M":[[14,74,46],[23,75,47]],"Q":[[44,54,24],[7,55,25]],"H":[[59,46,16],[1,47,17]]},"35":{"L":[[12,151,121],[7,152,122]],"M":[[12,75,47],[26,76,48]],"Q":[[39,54,24],[14,55,25]],"H":[[22,45,15],[41,46,16]]},"36":{"L":[[6,151,121],[14,152,122]],"M":[[6,75,47],[34,76,48]],"Q":[[46,54,24],[10,55,25]],"H":[[2,45,15],[64,46,16]]},"37":{"L":[[17,152,122],[4,153,123]],"M":[[29,74,46],[14,75,47]],"Q":[[49,54,24],[10,55,25]],"H":[[24,45,15],[46,46,16]]},"38":{"L":[[4,152,122],[18,153,123]],"M":[[13,74,46],[32,75,47]],"Q":[[48,54,24],[14,55,25]],"H":[[42,45,15],[32,46,16]]},"39":{"L":[[20,147,117],[4,148,118]],"M":[[40,75,47],[7,76,48]],"Q":[[43,54,24],[22,55,25]],"H":[[10,45,15],[67,46,16]]},"40":{"L":[[19,148,118],[6,149,119]],"M":[[18,75,47],[31,76,48]],"Q":[[34,54,24],[34,55,25]],"H":[[20,45,15],[61,46,16]]}},"align":{"2":[6,18],"3":[6,22],"4":[6,26],"5":[6,30],"6":[6,34],"7":[6,22,38],"8":[6,24,42],"9":[6,26,46],"10":[6,28,50],"11":[6,30,54],"12":[6,32,58],"13":[6,34,62],"14":[6,26,46,66],"15":[6,26,48,70],"16":[6,26,50,74],"17":[6,30,54,78],"18":[6,30,56,82],"19":[6,30,58,86],"20":[6,34,62,90],"21":[6,28,50,72,94],"22":[6,26,50,74,98],"23":[6,30,54,78,102],"24":[6,28,54,80,106],"25":[6,32,58,84,110],"26":[6,30,58,86,114],"27":[6,34,62,90,118],"28":[6,26,50,74,98,122],"29":[6,30,54,78,102,126],"30":[6,26,52,78,104,130],"31":[6,30,56,82,108,134],"32":[6,34,60,86,112,138],"33":[6,30,58,86,114,142],"34":[6,34,62,90,118,146],"35":[6,30,54,78,102,126,150],"36":[6,24,50,76,102,128,154],"37":[6,28,54,80,106,132,158],"38":[6,32,58,84,110,136,162],"39":[6,26,54,82,110,138,166],"40":[6,30,58,86,114,142,170]},"versionInfo":{"7":31892,"8":34236,"9":39577,"10":42195,"11":48118,"12":51042,"13":55367,"14":58893,"15":63784,"16":68472,"17":70749,"18":76311,"19":79154,"20":84390,"21":87683,"22":92361,"23":96236,"24":102084,"25":102881,"26":110507,"27":110734,"28":117786,"29":119615,"30":126325,"31":127568,"32":133589,"33":136944,"34":141498,"35":145311,"36":150283,"37":152622,"38":158308,"39":161089,"40":167017},"formatInfo":{"L":[30660,29427,32170,30877,26159,25368,27713,26998],"M":[21522,20773,24188,23371,17913,16590,20375,19104],"Q":[13663,12392,16177,14854,9396,8579,11994,11245],"H":[5769,5054,7399,6608,1890,597,3340,2107]}};

const EXP = new Uint8Array(512), LOG = new Uint8Array(256);
(() => { let x = 1;
  for (let i = 0; i < 255; i++) { EXP[i] = x; LOG[x] = i; x <<= 1; if (x & 0x100) x ^= 0x11d; }
  for (let i = 255; i < 512; i++) EXP[i] = EXP[i - 255];
})();
const mul = (a, b) => (a === 0 || b === 0) ? 0 : EXP[LOG[a] + LOG[b]];

function genPoly(n) {
  let g = [1];
  for (let i = 0; i < n; i++) {
    const ng = new Array(g.length + 1).fill(0);
    for (let j = 0; j < g.length; j++) { ng[j] ^= g[j]; ng[j + 1] ^= mul(g[j], EXP[i]); }
    g = ng;
  }
  return g;
}
function rsEncode(data, ecLen) {
  const g = genPoly(ecLen), res = new Uint8Array(data.length + ecLen);
  res.set(data);
  for (let i = 0; i < data.length; i++) {
    const coef = res[i]; if (!coef) continue;
    for (let j = 1; j < g.length; j++) res[i + j] ^= mul(g[j], coef);
  }
  return res.subarray(data.length);
}

function utf8Bytes(str) {
  const out = [];
  for (const ch of str) {
    const cp = ch.codePointAt(0);
    if (cp < 0x80) out.push(cp);
    else if (cp < 0x800) out.push(0xc0 | (cp >> 6), 0x80 | (cp & 63));
    else if (cp < 0x10000) out.push(0xe0 | (cp >> 12), 0x80 | ((cp >> 6) & 63), 0x80 | (cp & 63));
    else out.push(0xf0 | (cp >> 18), 0x80 | ((cp >> 12) & 63), 0x80 | ((cp >> 6) & 63), 0x80 | (cp & 63));
  }
  return Uint8Array.from(out);
}

const ccBits = (v) => (v <= 9 ? 8 : 16);
const groupsFor = (v, ec) => T.ecc[v][ec];
const dataCodewords = (v, ec) => groupsFor(v, ec).reduce((s, g) => s + g[0] * g[2], 0);
const totalCodewords = (v, ec) => groupsFor(v, ec).reduce((s, g) => s + g[0] * g[1], 0);

function pickVersion(byteLen, ec, minVersion) {
  for (let v = Math.max(1, minVersion || 1); v <= 40; v++) {
    const cap = dataCodewords(v, ec) * 8;
    if (4 + ccBits(v) + byteLen * 8 <= cap) return v;
  }
  return null;
}

function buildCodewords(bytes, v, ec, padCompat) {
  const bits = [];
  const push = (val, len) => { for (let i = len - 1; i >= 0; i--) bits.push((val >> i) & 1); };
  push(0b0100, 4);                 // byte mode
  push(bytes.length, ccBits(v));
  for (const b of bytes) push(b, 8);

  const capBits = dataCodewords(v, ec) * 8;
  for (let i = 0; i < 4 && bits.length < capBits; i++) bits.push(0); // terminator
  if (padCompat) { for (let i = 0; i < 8 - (bits.length % 8); i++) bits.push(0); } // segno quirk
  else while (bits.length % 8) bits.push(0);                         // byte align (ISO 7.4.10)

  const cw = [];
  for (let i = 0; i < bits.length; i += 8) {
    let b = 0; for (let j = 0; j < 8; j++) b = (b << 1) | bits[i + j];
    cw.push(b);
  }
  const pads = [0xec, 0x11];
  for (let i = 0; cw.length < dataCodewords(v, ec); i++) cw.push(pads[i % 2]);

  // split into blocks, RS-encode, interleave
  const dataBlocks = [], ecBlocks = [];
  let pos = 0;
  for (const [nb, ntotal, ndata] of groupsFor(v, ec)) {
    for (let i = 0; i < nb; i++) {
      const d = Uint8Array.from(cw.slice(pos, pos + ndata)); pos += ndata;
      dataBlocks.push(d);
      ecBlocks.push(rsEncode(d, ntotal - ndata));
    }
  }
  const out = [];
  const maxData = Math.max(...dataBlocks.map(b => b.length));
  for (let i = 0; i < maxData; i++) for (const b of dataBlocks) if (i < b.length) out.push(b[i]);
  const maxEc = Math.max(...ecBlocks.map(b => b.length));
  for (let i = 0; i < maxEc; i++) for (const b of ecBlocks) if (i < b.length) out.push(b[i]);
  return out;
}

function makeMatrix(v) {
  const size = 17 + 4 * v;
  const m = Array.from({ length: size }, () => new Int8Array(size).fill(-1)); // -1 = free data cell
  const fn = Array.from({ length: size }, () => new Uint8Array(size));        // 1 = function module
  const set = (r, c, val) => {
    if (r < 0 || r >= size || c < 0 || c >= size) return;
    m[r][c] = val; fn[r][c] = 1;
  };

  const finder = (R, C) => {
    for (let r = -1; r <= 7; r++) for (let c = -1; c <= 7; c++) {
      const inR = r >= 0 && r <= 6, inC = c >= 0 && c <= 6;
      const dark = inR && inC &&
        (r === 0 || r === 6 || c === 0 || c === 6 || (r >= 2 && r <= 4 && c >= 2 && c <= 4));
      set(R + r, C + c, dark ? 1 : 0);
    }
  };
  finder(0, 0); finder(0, size - 7); finder(size - 7, 0);

  if (v >= 2) {
    const pos = T.align[v];
    for (const r of pos) for (const c of pos) {
      if ((r <= 8 && c <= 8) || (r <= 8 && c >= size - 9) || (r >= size - 9 && c <= 8)) continue;
      for (let dr = -2; dr <= 2; dr++) for (let dc = -2; dc <= 2; dc++)
        set(r + dr, c + dc, Math.max(Math.abs(dr), Math.abs(dc)) !== 1 ? 1 : 0);
    }
  }

  for (let i = 8; i < size - 8; i++) { const b = i % 2 === 0 ? 1 : 0; set(6, i, b); set(i, 6, b); }
  set(4 * v + 9, 8, 0); // dark module -- light during mask evaluation, set by applyFormat

  // reserve format-information areas
  for (let i = 0; i < 9; i++) {
    if (m[8][i] === -1) set(8, i, 0);
    if (m[i][8] === -1) set(i, 8, 0);
  }
  for (let i = 0; i < 8; i++) { set(8, size - 1 - i, 0); set(size - 1 - i, 8, 0); }
  // reserve version-information areas
  if (v >= 7) for (let i = 0; i < 18; i++) {
    const r = Math.floor(i / 3), c = i % 3;
    set(size - 11 + c, r, 0); set(r, size - 11 + c, 0);
  }
  return { m, fn };
}

function placeData(m, codewords) {
  const size = m.length;
  let bitIdx = 0;
  const nextBit = () => {
    const byte = codewords[bitIdx >> 3];
    const bit = byte === undefined ? 0 : (byte >> (7 - (bitIdx & 7))) & 1;
    bitIdx++; return bit;
  };
  let up = true;
  for (let right = size - 1; right > 0; right -= 2) {
    if (right === 6) right = 5;
    for (let i = 0; i < size; i++) {
      const row = up ? size - 1 - i : i;
      for (const col of [right, right - 1]) {
        if (m[row][col] !== -1) continue;
        m[row][col] = nextBit() ? 1 : 0;
      }
    }
    up = !up;
  }
}

const MASKS = [
  (r, c) => (r + c) % 2 === 0,
  (r) => r % 2 === 0,
  (r, c) => c % 3 === 0,
  (r, c) => (r + c) % 3 === 0,
  (r, c) => (Math.floor(r / 2) + Math.floor(c / 3)) % 2 === 0,
  (r, c) => ((r * c) % 2) + ((r * c) % 3) === 0,
  (r, c) => (((r * c) % 2) + ((r * c) % 3)) % 2 === 0,
  (r, c) => (((r + c) % 2) + ((r * c) % 3)) % 2 === 0,
];

// ISO/IEC 18004:2015 7.8.3, Table 11 -- N1=3, N2=3, N3=40, N4=10.
// The quiet zone counts as light area for the 1:1:3:1:1 rule, so a pattern
// flush against the symbol edge still scores.
function n3Occurrences(seq, size) {
  const pat = [1, 0, 1, 1, 1, 0, 1];
  const findFrom = (from) => {
    for (let i = from; i + 7 <= size; i++) {
      let hit = true;
      for (let k = 0; k < 7; k++) if (seq[i + k] !== pat[k]) { hit = false; break; }
      if (hit) return i;
    }
    return -1;
  };
  const anyDark = (lo, hi) => { for (let i = Math.max(lo, 0); i < Math.min(hi, size); i++) if (seq[i]) return true; return false; };

  let count = 0, idx = findFrom(0);
  while (idx !== -1) {
    let offset = idx + 7;
    if (idx === 0 || idx === size - 7 || !anyDark(idx - 4, idx) || !anyDark(offset, offset + 4)) count += 40;
    else offset = idx + 4;
    idx = findFrom(offset);
  }
  return count;
}

function penalty(g) {
  const n = g.length;
  let score = 0;
  const runScore = (len) => (len >= 5 ? len - 2 : 0); // N1: 3 + (len - 5)

  for (let i = 0; i < n; i++) {
    let rl = 1, cl = 1;
    for (let j = 1; j < n; j++) {
      if (g[i][j] === g[i][j - 1]) rl++; else { score += runScore(rl); rl = 1; }
      if (g[j][i] === g[j - 1][i]) cl++; else { score += runScore(cl); cl = 1; }
    }
    score += runScore(rl) + runScore(cl);
  }

  for (let r = 0; r < n - 1; r++) for (let c = 0; c < n - 1; c++) { // N2
    const v = g[r][c];
    if (v === g[r][c + 1] && v === g[r + 1][c] && v === g[r + 1][c + 1]) score += 3;
  }

  const col = new Array(n);
  for (let i = 0; i < n; i++) { // N3
    for (let j = 0; j < n; j++) col[j] = g[j][i];
    score += n3Occurrences(g[i], n) + n3Occurrences(col, n);
  }

  let dark = 0; // N4
  for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) dark += g[r][c];
  score += 10 * Math.floor(Math.abs((dark * 100) / (n * n) - 50) / 5);
  return score;
}

function applyFormat(g, v, ec, mask) {
  const size = g.length, fmt = T.formatInfo[ec][mask];
  const bit = (i) => (fmt >> i) & 1;
  for (let i = 0; i < 15; i++) {
    const b = bit(i);
    if (i < 6) g[i][8] = b;
    else if (i < 8) g[i + 1][8] = b;
    else g[size - 15 + i][8] = b;
  }
  for (let i = 0; i < 15; i++) {
    const b = bit(i);
    if (i < 8) g[8][size - i - 1] = b;
    else if (i < 9) g[8][15 - i] = b;
    else g[8][14 - i] = b;
  }
  g[size - 8][8] = 1; // dark module

  if (v >= 7) {
    const vi = T.versionInfo[v];
    for (let i = 0; i < 18; i++) {
      const b = (vi >> i) & 1, r = Math.floor(i / 3), c = i % 3;
      g[r][size - 11 + c] = b;
      g[size - 11 + c][r] = b;
    }
  }
}

function encodeQR(text, ecLevel = 'M', minVersion = 1, forceMask = null, padCompat = false) {
  const ec = ecLevel.toUpperCase();
  if (!'LMQH'.includes(ec)) throw new Error('ECC level must be L, M, Q or H');
  const bytes = utf8Bytes(text);
  const v = pickVersion(bytes.length, ec, minVersion);
  if (!v) throw new Error('Content too long for a QR code at ECC level ' + ec);
  const codewords = buildCodewords(bytes, v, ec, padCompat);
  const { m: base, fn } = makeMatrix(v);
  placeData(base, codewords);

  // ISO/IEC 18004:2015 7.8 -- masks are evaluated BEFORE format/version info is written.
  let best = null;
  for (let mask = 0; mask < 8; mask++) {
    if (forceMask !== null && mask !== forceMask) continue;
    const g = base.map((row, r) =>
      Array.from(row, (val, c) => (fn[r][c] ? val : (MASKS[mask](r, c) ? val ^ 1 : val))));
    const s = penalty(g);
    if (!best || s < best.score) best = { score: s, grid: g, mask };
  }
  applyFormat(best.grid, v, ec, best.mask);
  return {
    size: base.length, modules: best.grid, version: v, ecLevel: ec, mask: best.mask,
    byteLength: bytes.length, capacityBytes: dataCodewords(v, ec),
  };
}


/* ---------------------------------------------------------------- rendering */

/**
 * Render a QR result as a print-ready SVG string.
 * Geometry is expressed in millimetres so print output is physically exact.
 */
function toSVG(qr, opts = {}) {
  const {
    sizeMM = 40,          // finished symbol width, excluding the quiet zone
    quietZone = 4,        // in modules; ISO 18004 requires >= 4
    dark = '#000000',
    light = '#FFFFFF',
    label = null,         // human-readable URL printed under the code
    labelMM = 3.2,
  } = opts;

  const n = qr.size;
  const total = n + quietZone * 2;
  const unit = sizeMM / n;                 // mm per module
  const wMM = total * unit;
  const labelBlock = label ? labelMM * 2.2 : 0;
  const hMM = wMM + labelBlock;

  // Merge horizontal runs into single rects -- far fewer path nodes for RIPs.
  let rects = '';
  for (let r = 0; r < n; r++) {
    let c = 0;
    while (c < n) {
      if (!qr.modules[r][c]) { c++; continue; }
      let run = 1;
      while (c + run < n && qr.modules[r][c + run]) run++;
      const x = (c + quietZone) * unit, y = (r + quietZone) * unit;
      rects += `<rect x="${round(x)}" y="${round(y)}" width="${round(run * unit)}" height="${round(unit)}"/>`;
      c += run;
    }
  }

  const text = label
    ? `<text x="${round(wMM / 2)}" y="${round(wMM + labelMM * 1.4)}" font-family="Helvetica,Arial,sans-serif" ` +
      `font-size="${round(labelMM)}" text-anchor="middle" fill="${dark}">${escapeXML(label)}</text>`
    : '';

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${round(wMM)}mm" height="${round(hMM)}mm" viewBox="0 0 ${round(wMM)} ${round(hMM)}" shape-rendering="crispEdges">
<desc>QR ${qr.version}-${qr.ecLevel} mask ${qr.mask}${label ? ' -- ' + escapeXML(label) : ''}</desc>
<rect width="${round(wMM)}" height="${round(hMM)}" fill="${light}"/>
<g fill="${dark}">${rects}</g>${text}
</svg>`;
}

const round = (v) => Math.round(v * 10000) / 10000;
const escapeXML = (s) => String(s).replace(/[<>&"']/g, (ch) =>
  ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&apos;' }[ch]));

/**
 * Smallest symbol width (mm) that a typical phone camera resolves from
 * `distanceMM` away. Rule of thumb: symbol width >= distance / 10, and never
 * below a module size of `minModuleMM`.
 */
function minPrintSizeMM(qr, distanceMM, minModuleMM = 0.4) {
  return Math.max(distanceMM / 10, qr.size * minModuleMM);
}

const API = { encodeQR, toSVG, minPrintSizeMM, dataCodewords, totalCodewords,
  // exposed for qr-decoder.js and the test suite
  _internals: { makeMatrix, MASKS, TABLES: T } };
if (typeof module !== 'undefined' && module.exports) module.exports = API;
if (typeof window !== 'undefined') window.QR = API;
