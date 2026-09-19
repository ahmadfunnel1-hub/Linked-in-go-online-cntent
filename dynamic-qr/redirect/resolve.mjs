/*!
 * Pure routing logic for the dynamic QR redirect. No Worker runtime needed,
 * so it can be tested directly -- see ../test/worker.test.mjs.
 */

/* 302, never 301.
 * A 301 is cached by browsers and intermediaries essentially forever. Repoint a
 * campaign later and everyone who already scanned keeps landing on the old
 * destination, with no way to clear their cache. A permanent redirect turns a
 * dynamic QR code back into a static one. */
export const REDIRECT_STATUS = 302;

/**
 * @param {object} links   the link map (redirect/links.json)
 * @param {string} requestUrl  the URL that was scanned
 * @returns {{status: number, location: string, entry: object|null, slug: string}}
 */
export function resolve(links, requestUrl) {
  const url = new URL(requestUrl);
  const slug = url.pathname.replace(/^\/+|\/+$/g, '').toLowerCase();

  if (!slug || slug === 'favicon.ico')
    return { status: REDIRECT_STATUS, location: links._fallback, entry: null, slug };

  const entry = links[slug];
  if (!entry || typeof entry !== 'object' || !entry.to) {
    // Unknown slug: send them somewhere useful rather than showing an error.
    return { status: 404, location: links._fallback, entry: null, slug };
  }

  const target = new URL(entry.to);

  // Attribution. GHL reads these off the landing page and stores them on the
  // contact when a form is submitted, so leads carry their source without
  // needing a webhook on every scan.
  const utm = {
    utm_source: 'qr',
    utm_medium: 'print',
    utm_campaign: entry.campaign || slug,
  };
  for (const [k, v] of Object.entries(utm))
    if (!target.searchParams.has(k)) target.searchParams.set(k, v);

  // Pass through anything already on the scanned URL (e.g. per-table codes:
  // go.example.com/menu?t=14) without letting it clobber the UTMs above.
  for (const [k, v] of url.searchParams)
    if (!target.searchParams.has(k)) target.searchParams.set(k, v);

  return { status: REDIRECT_STATUS, location: target.toString(), entry, slug };
}
