/*!
 * qr-decoder.js -- reads a QR matrix produced by qr-encoder.js back to text.
 *
 * This exists to verify the encoder rather than to read photographs: it takes a
 * clean module matrix, not an image. It recovers the format information from
 * the symbol itself and checks every Reed-Solomon syndrome, so a symbol that
 * round-trips here is one a real scanner can read.
 */
const { _internals } = require('./qr-encoder.js');
const { makeMatrix, MASKS, TABLES: T } = _internals;

const EXP = new Uint8Array(512), LOG = new Uint8Array(256);
(() => { let x = 1;
  for (let i = 0; i < 255; i++) { EXP[i] = x; LOG[x] = i; x <<= 1; if (x & 0x100) x ^= 0x11d; }
  for (let i = 255; i < 512; i++) EXP[i] = EXP[i - 255];
})();
const mul = (a, b) => (!a || !b) ? 0 : EXP[LOG[a] + LOG[b]];

function readFormat(grid) {
  const size = grid.length;
  let raw = 0;
  for (let i = 0; i < 15; i++) {
    const b = i < 6 ? grid[i][8] : i < 8 ? grid[i + 1][8] : grid[size - 15 + i][8];
    raw |= b << i;
  }
  for (const ec of ['L', 'M', 'Q', 'H'])
    for (let m = 0; m < 8; m++)
      if (T.formatInfo[ec][m] === raw) return { ec, mask: m };
  throw new Error('unrecognised format information: 0b' + raw.toString(2));
}

function decode(grid) {
  const size = grid.length, v = (size - 17) / 4;
  if (!Number.isInteger(v) || v < 1 || v > 40) throw new Error('not a QR matrix: size ' + size);
  const { fn } = makeMatrix(v);
  const { ec, mask } = readFormat(grid);

  const bits = [];
  let up = true;
  for (let right = size - 1; right > 0; right -= 2) {
    if (right === 6) right = 5;
    for (let i = 0; i < size; i++) {
      const row = up ? size - 1 - i : i;
      for (const col of [right, right - 1]) {
        if (fn[row][col]) continue;
        bits.push(MASKS[mask](row, col) ? grid[row][col] ^ 1 : grid[row][col]);
      }
    }
    up = !up;
  }
  const stream = [];
  for (let i = 0; i + 8 <= bits.length; i += 8) {
    let b = 0; for (let j = 0; j < 8; j++) b = (b << 1) | bits[i + j];
    stream.push(b);
  }

  const blocks = [];
  for (const [nb, ntotal, ndata] of T.ecc[v][ec])
    for (let i = 0; i < nb; i++) blocks.push({ nd: ndata, ne: ntotal - ndata, data: [], ecc: [] });

  let p = 0;
  for (let i = 0; i < Math.max(...blocks.map(b => b.nd)); i++)
    for (const b of blocks) if (i < b.nd) b.data.push(stream[p++]);
  for (let i = 0; i < Math.max(...blocks.map(b => b.ne)); i++)
    for (const b of blocks) if (i < b.ne) b.ecc.push(stream[p++]);

  blocks.forEach((b, bi) => {
    const poly = b.data.concat(b.ecc);
    for (let s = 0; s < b.ne; s++) {
      let acc = 0;
      for (const coef of poly) acc = mul(acc, EXP[s]) ^ coef;
      if (acc !== 0) throw new Error(`Reed-Solomon syndrome ${s} non-zero in block ${bi}`);
    }
  });

  const cw = [].concat(...blocks.map(b => b.data));
  const out = [];
  for (const b of cw) for (let i = 7; i >= 0; i--) out.push((b >> i) & 1);
  let idx = 0;
  const take = (n) => { let x = 0; for (let i = 0; i < n; i++) x = (x << 1) | out[idx++]; return x; };
  const mode = take(4);
  if (mode !== 0b0100) throw new Error('expected byte mode, got 0b' + mode.toString(2));
  const count = take(v <= 9 ? 8 : 16);
  const bytes = [];
  for (let i = 0; i < count; i++) bytes.push(take(8));
  return { text: Buffer.from(bytes).toString('utf8'), version: v, ecLevel: ec, mask, byteLength: count };
}

module.exports = { decode };
