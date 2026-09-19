/*!
 * Tests the redirect resolver. `node test/worker.test.js`
 *
 * These redirects sit behind printed artwork that cannot be recalled, so the
 * routing rules are worth pinning down.
 */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { resolve } from '../redirect/resolve.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const links = JSON.parse(readFileSync(join(here, '../redirect/links.json'), 'utf8'));

let pass = 0, fail = 0;
const failures = [];
const check = (name, fn) => {
  try { fn(); pass++; } catch (e) { fail++; failures.push(`${name}: ${e.message}`); }
};
const assert = (c, m) => { if (!c) throw new Error(m); };

check('known slug redirects to its destination', () => {
  const r = resolve(links, 'https://go.example.com/menu');
  assert(r.status === 302, `expected 302, got ${r.status}`);
  assert(r.location.startsWith(links.menu.to.split('?')[0]), `wrong destination: ${r.location}`);
});

check('redirect is temporary, so campaigns stay repointable', () => {
  assert(resolve(links, 'https://go.example.com/menu').status === 302,
    'a 301 is cached indefinitely and would freeze the destination');
});

check('UTMs are attached for GHL attribution', () => {
  const u = new URL(resolve(links, 'https://go.example.com/menu').location);
  assert(u.searchParams.get('utm_source') === 'qr', 'missing utm_source');
  assert(u.searchParams.get('utm_medium') === 'print', 'missing utm_medium');
  assert(u.searchParams.get('utm_campaign') === links.menu.campaign,
    `utm_campaign should be the campaign name, got ${u.searchParams.get('utm_campaign')}`);
});

check('scanned query params pass through', () => {
  const u = new URL(resolve(links, 'https://go.example.com/menu?t=14').location);
  assert(u.searchParams.get('t') === '14', 'per-table parameter was dropped');
});

check('scanned params cannot overwrite attribution', () => {
  const u = new URL(resolve(links, 'https://go.example.com/menu?utm_source=spoofed').location);
  assert(u.searchParams.get('utm_source') === 'qr', 'utm_source was overwritten by the query string');
});

check('trailing slashes and case do not matter', () => {
  for (const path of ['/menu', '/menu/', '/MENU', '//menu//']) {
    const r = resolve(links, 'https://go.example.com' + path);
    assert(r.entry !== null, `${path} failed to resolve`);
  }
});

check('unknown slug falls back instead of erroring', () => {
  const r = resolve(links, 'https://go.example.com/typo');
  assert(r.status === 404, `expected 404, got ${r.status}`);
  assert(r.location === links._fallback, 'should land on the fallback URL');
});

check('bare host and favicon hit the fallback', () => {
  for (const path of ['/', '/favicon.ico']) {
    const r = resolve(links, 'https://go.example.com' + path);
    assert(r.location === links._fallback, `${path} should use the fallback`);
  }
});

check('metadata keys are not routable slugs', () => {
  const r = resolve(links, 'https://go.example.com/_fallback');
  assert(r.entry === null, '_fallback must not resolve as a campaign');
});

check('every configured slug resolves', () => {
  for (const [slug, entry] of Object.entries(links)) {
    if (slug.startsWith('_')) continue;
    const r = resolve(links, 'https://go.example.com/' + slug);
    assert(r.entry !== null, `${slug} did not resolve`);
    assert(new URL(entry.to).protocol === 'https:', `${slug} destination must be https`);
  }
});

console.log(`\n${pass} passed, ${fail} failed`);
if (fail) { console.log('\n' + failures.join('\n')); process.exit(1); }
