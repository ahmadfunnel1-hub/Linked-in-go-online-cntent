#!/usr/bin/env node
/*!
 * Print-ready QR generator.
 *
 *   node generate-qr.js --url https://go.example.com/menu --out menu.svg
 *   node generate-qr.js --url https://go.example.com/menu --ecc H --size 60 --label
 *
 * Output is SVG in real millimetres, so the printer gets exact physical
 * geometry. Never hand a printer an upscaled PNG.
 */
const fs = require('fs');
const { encodeQR, toSVG, minPrintSizeMM } = require('./qr-encoder.js');

const argv = process.argv.slice(2);
const arg = (name, fallback) => {
  const i = argv.indexOf('--' + name);
  return i === -1 ? fallback : (argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : true);
};

const url = arg('url');
if (!url || url === true) {
  console.error(`usage: node generate-qr.js --url <url> [options]

  --url <url>        destination encoded in the symbol (required)
  --out <file>       output path                        (default: qr.svg)
  --ecc L|M|Q|H      error correction level             (default: Q)
  --size <mm>        symbol width in mm, quiet zone excluded (default: 40)
  --quiet <modules>  quiet zone width in modules        (default: 4, the ISO minimum)
  --label            print the URL under the symbol
  --distance <mm>    report the minimum size for this scan distance`);
  process.exit(1);
}

const ecc = String(arg('ecc', 'Q')).toUpperCase();
const sizeMM = Number(arg('size', 40));
const quietZone = Number(arg('quiet', 4));
const out = arg('out', 'qr.svg');

if (quietZone < 4) console.warn('warning: a quiet zone below 4 modules breaks ISO 18004 and many scanners');

let qr;
try {
  qr = encodeQR(url, ecc);
} catch (e) {
  console.error('error: ' + e.message);
  process.exit(1);
}

const label = arg('label', false)
  ? url.replace(/^https?:\/\//, '').replace(/\/$/, '')
  : null;

fs.writeFileSync(out, toSVG(qr, { sizeMM, quietZone, label }));

const moduleMM = sizeMM / qr.size;
console.log(`wrote ${out}`);
console.log(`  content    ${url}`);
console.log(`  symbol     version ${qr.version}, ${qr.size}x${qr.size} modules, ECC ${qr.ecLevel}, mask ${qr.mask}`);
console.log(`  payload    ${qr.byteLength} of ${qr.capacityBytes} bytes used`);
console.log(`  printed    ${sizeMM}mm wide, ${moduleMM.toFixed(3)}mm per module`);

if (moduleMM < 0.4)
  console.log(`  WARNING    modules below 0.4mm scan unreliably -- print at ${(qr.size * 0.4).toFixed(0)}mm or larger`);

const distance = Number(arg('distance', 0));
if (distance)
  console.log(`  at ${distance}mm  needs at least ${minPrintSizeMM(qr, distance).toFixed(0)}mm wide`);
