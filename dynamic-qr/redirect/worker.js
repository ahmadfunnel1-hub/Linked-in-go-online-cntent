/*!
 * Dynamic QR redirect -- Cloudflare Worker.
 *
 * The printed QR encodes https://go.<yourdomain>/<slug>. This Worker resolves
 * <slug> to whatever that campaign currently points at. Repointing a printed
 * code is a one-line edit to links.json plus a redeploy; the artwork on the
 * wall never changes again.
 *
 * The domain is yours, so no vendor can pause your printed assets. That is the
 * whole point -- see ../README.md.
 *
 * Deploy:  npx wrangler deploy
 */
import links from './links.json';
import { resolve, REDIRECT_STATUS } from './resolve.mjs';

export default {
  async fetch(request, env, ctx) {
    const { status, location, entry, slug } = resolve(links, request.url);

    if (entry && env.GHL_WEBHOOK_URL)
      ctx.waitUntil(notifyGHL(env.GHL_WEBHOOK_URL, slug, entry, request));

    return new Response(null, {
      status,
      headers: {
        Location: location,
        // Without this, a repointed campaign only takes effect once caches expire.
        'Cache-Control': 'no-store, no-cache, must-revalidate',
        'Referrer-Policy': 'no-referrer-when-downgrade',
      },
    });
  },
};

/*
 * Optional. Fires a GHL inbound-webhook workflow on each scan.
 *
 * Use it sparingly. A scan is anonymous -- if the workflow creates a contact
 * you will fill the CRM with empty records, one per passer-by. Point it at a
 * workflow that only counts or notifies, and let real contacts arrive through
 * the form on the destination page, where the UTMs above attribute them.
 *
 * GHL creates custom fields automatically from the payload keys, so nothing
 * needs setting up on the GHL side first.
 */
async function notifyGHL(webhookUrl, slug, entry, request) {
  try {
    await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        qr_slug: slug,
        qr_campaign: entry.campaign || slug,
        qr_owner: entry.owner || '',
        qr_destination: entry.to,
        qr_scanned_at: new Date().toISOString(),
        qr_country: request.headers.get('cf-ipcountry') || '',
        qr_user_agent: request.headers.get('user-agent') || '',
      }),
    });
  } catch {
    // Never let a tracking failure block the redirect -- the scan must always land.
  }
}
