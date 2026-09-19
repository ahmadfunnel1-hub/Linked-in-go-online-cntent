/*!
 * Exact matrix comparison against the `segno` reference library.
 *   python3 test/make-reference.py && node test/cross-check-segno.js
 *
 * Run with segno's padding quirk enabled (see the note in qr-encoder.js):
 * segno appends a whole zero codeword even when the bit stream already ends on
 * a codeword boundary, which in byte mode it always does. Everything else --
 * encoding, Reed-Solomon, interleaving, placement, masking, penalty scoring,
 * format and version information -- must match bit for bit.
 */
const fs = require('fs');
const path = require('path');
const { encodeQR } = require('../qr-encoder.js');

const refPath = path.join(__dirname, 'reference.json');
if (!fs.existsSync(refPath)) {
  console.error('missing test/reference.json -- run: python3 test/make-reference.py');
  process.exit(2);
}
const cases = JSON.parse(fs.readFileSync(refPath, 'utf8'));

let match = 0;
const mismatches = [];
for (const c of cases) {
  const r = encodeQR(c.text, c.ec, 1, null, /* padCompat */ true);
  let same = r.size === c.size && r.version === c.version && r.mask === c.mask;
  if (same) outer:
    for (let i = 0; i < c.size; i++)
      for (let j = 0; j < c.size; j++)
        if (r.modules[i][j] !== c.matrix[i][j]) { same = false; break outer; }
  if (same) match++;
  else mismatches.push(`len=${c.text.length} ecc=${c.ec} v${c.version} ` +
                       `mask expected ${c.mask}, got ${r.mask}`);
}
const versions = [...new Set(cases.map(c => c.version))].sort((a, b) => a - b);
console.log(`versions covered: ${versions.join(',')}`);
console.log(`${match}/${cases.length} matrices byte-identical to segno`);
if (mismatches.length) { console.log('\n' + mismatches.join('\n')); process.exit(1); }
