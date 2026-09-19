# Dynamic QR codes you own

Rebuilding a paused vendor QR code as one that cannot be taken away, with the
destination and the tracking living in GHL.

---

## 1. The old code cannot be revived

A QR code is a picture of a string. The paused code is a picture of
`qr.mobi/f4c17dea`, and `qr.mobi` is the vendor's domain.

Two consequences, and the second is the one that matters:

- **Cloning the picture is trivial.** Encode the same string and you get a
  pixel-identical symbol. `node generate-qr.js --url https://qr.mobi/f4c17dea`
  produces it in a second.
- **The clone is worthless.** It still resolves through the vendor's servers,
  on the account that is locked and paused. The pattern was never the asset —
  the destination was.

There is also no way to be certain what the old symbol encodes. The caption
under a QR code is a label the dashboard prints, not necessarily the bytes in
the symbol: `https://qr.mobi/f4c17dea` and `http://qr.mobi/f4c17dea` display the
same and encode differently. It does not matter, because both are dead.

So the printed material has to be reissued. Do it once, correctly, so it is the
last time.

## 2. The rule that prevents a repeat

> **The QR code encodes a URL on a domain you own. Nothing else, ever.**

That is the entire lesson of the lockout. A printed code is permanent — it is
on walls, menus, vehicles, packaging. Whoever controls the domain in that code
controls the asset. Rent the domain from a QR vendor and they can pause your
printed material, as just happened.

This applies to GHL too. **Do not print a `link.msgsndr.com` trigger link or a
GHL funnel URL.** They work, and they are fine as *destinations* — but if the
sub-account is paused, the client churns, or you migrate them, every printed
code dies exactly the way the vendor's did. DNS is the only layer you own
outright.

## 3. Architecture

```
  printed QR  ──▶  https://go.<clientdomain>/menu     ← never changes again
                            │                            (you own the DNS)
                            ▼
                   Cloudflare Worker                  ← swap destinations here
                   redirect/links.json                  (free, instant)
                            │
                            ▼
                   GHL funnel / booking / form        ← the campaign
                   + utm_source=qr&utm_medium=print
                            │
                            ▼
                   GHL contact, attributed
```

Three layers, each replaceable without touching the one above it. The printed
artwork is pinned to layer 1, which is the only layer that can never be taken
from you.

## 4. Setup

**1. Pick the host.** A short subdomain on the client's existing domain —
`go.clientdomain.com`. Short matters: fewer characters means a lower QR version,
larger modules at the same printed size, and an easier scan. Put the zone on
Cloudflare (free tier is enough).

**2. Configure the campaigns.** Edit `redirect/links.json`:

```json
{
  "_fallback": "https://clientdomain.com",
  "menu": {
    "to": "https://api.leadconnectorhq.com/widget/...",
    "campaign": "table_tent",
    "owner": "Client A",
    "printedOn": "table tents, spring 2026"
  }
}
```

Keep `printedOn` accurate. When someone asks a year from now whether a slug is
safe to repoint, that field is the answer.

**3. Deploy.** Set the route in `redirect/wrangler.toml` to your host, then
`npx wrangler deploy`. Confirm `https://go.clientdomain.com/menu` lands on the
right page before anything goes to print.

**4. Generate the artwork.**

```bash
node generate-qr.js --url https://go.clientdomain.com/menu \
                    --ecc Q --size 50 --label --out menu.svg
```

**5. Test before printing.** Scan the actual proof on the actual material with
iOS Camera, Android Camera, and one third-party scanner, at the real distance.
Then print.

To repoint a campaign later: edit `links.json`, redeploy. The printed code is
untouched.

## 5. GHL wiring

**Destination.** Build the page in GHL as usual. The Worker appends
`utm_source=qr`, `utm_medium=print` and `utm_campaign=<campaign>` to the
destination, so any form submission on that page carries its attribution onto
the contact. This is the whole tracking story for most codes — no webhook
needed.

**Parallel campaigns on one page.** Where several printed codes land on the same
funnel, isolate the workflows on `utm_campaign`, not on tags. Two workflows
triggered from the same page apply their tags simultaneously and race; the UTM
value is carried by the visit itself and does not. Give each slug its own
`campaign` value and gate each workflow on it.

**Per-scan tracking (optional).** Create a workflow with an *Inbound Webhook*
trigger, then:

```bash
npx wrangler secret put GHL_WEBHOOK_URL
```

GHL creates the custom fields from the payload keys automatically — `qr_slug`,
`qr_campaign`, `qr_destination`, `qr_scanned_at`, `qr_country` — so there is no
field setup first.

Use this sparingly. A scan is anonymous. If the workflow creates a contact you
will fill the CRM with one empty record per passer-by, and the sub-account's
contact count is what you pay for. Point it at a workflow that counts or
notifies, and let real people become contacts by filling in the form. For plain
scan volume, Cloudflare's own analytics already answer the question for free.

## 6. Print specification

| | |
|---|---|
| **Error correction** | `Q` (25%) for print. `H` (30%) only if a logo covers the centre — it costs capacity and makes the symbol denser. `M` is fine for screens. |
| **Size** | Symbol width ≥ scan distance ÷ 10. A code read from 1.5 m needs to be ≥ 150 mm. `--distance` prints the number for you. |
| **Module size** | Never below 0.4 mm. The generator warns you. |
| **Quiet zone** | 4 modules clear on all sides, per ISO 18004. It is in the SVG — do not let a designer crop it or run artwork into it. |
| **Contrast** | Dark on light. Not inverted: plenty of scanners fail light-on-dark. Avoid gradients behind the symbol. |
| **Format** | SVG or PDF to the printer. Never upscale a PNG. |
| **Surfaces** | Test on curved, reflective, or stretched material (bottles, vehicle wrap, fabric) before committing to a run. |

## 7. If you recover the vendor account

Worth 30 minutes, because it is the only thing that rescues material already in
the field.

To identify the vendor: check the card statement, search the inbox for the
signup receipt, or scan the code and see where it lands.

To recover: password reset on the billing email; failing that, the vendor's
support with the invoice ID, the last four digits of the card, and the code
`f4c17dea` as proof of ownership.

**If you get in, do not simply unpause it.** Repoint the vendor code at
`https://go.clientdomain.com/<slug>` and leave it there. Every existing printed
code then flows through infrastructure you own, and the vendor becomes a
disposable hop you can stop paying for whenever you like. That converts a
hostage asset into a permanent one without reprinting anything.

## 8. Moving the rest of the business into GHL

The QR code is one asset. The same question applies to everything else the
business rents:

- [ ] Domain and DNS — on an account the client or the agency owns, not a vendor's
- [ ] Printed QR codes — on `go.<clientdomain>`, this repo
- [ ] Link shorteners in bio / print — same treatment, same reason
- [ ] Forms and landing pages — rebuilt as GHL funnels
- [ ] Contact list — exported and imported before any subscription lapses
- [ ] Booking / calendar — GHL calendars
- [ ] Email and SMS sending — GHL, with the sending domain verified
- [ ] Review and reputation links — repointed through `go.<clientdomain>`
- [ ] WhatsApp / WABA — registered under the **client's** Meta Business Manager, so the client owns the number outright

Export everything from a tool *before* cancelling it. A paused account is a
locked account.

## 9. This repo

```
qr-encoder.js        QR encoder, no dependencies, ISO/IEC 18004, byte mode, v1-40, ECC L/M/Q/H
qr-decoder.js        reads a matrix back; used to verify the encoder
generate-qr.js       CLI -> print-ready SVG in real millimetres
redirect/resolve.mjs routing logic for the redirect
redirect/worker.js   Cloudflare Worker
redirect/links.json  slug -> destination map; this is the file you edit
test/                verification suite
```

```bash
npm test                          # round-trip + redirect routing, no dependencies
npm run test:cross-check          # exact comparison against segno (needs: pip install segno)
```

### On trusting the encoder

A QR generator that is subtly wrong produces symbols that scan on your phone and
fail on a customer's. This one is checked two ways:

- **Round-trip.** Every symbol is decoded back from its own matrix, recovering
  the format information from the symbol and verifying that all Reed-Solomon
  syndromes are zero. 141 cases across versions 1–40 and all four ECC levels.
- **Cross-check.** Matrices are compared bit for bit against
  [`segno`](https://github.com/heuer/segno), an independent implementation.
  52/52 identical.

One deliberate difference from segno: ISO 18004 §7.4.10 adds padding bits only
when the bit stream does not already end on a codeword boundary. segno appends a
whole zero codeword even when it does, which in byte mode is always. Both scan
identically — the trailing bytes are padding either way — and the cross-check
has a flag to reproduce segno's behaviour so everything else can be compared
exactly.
