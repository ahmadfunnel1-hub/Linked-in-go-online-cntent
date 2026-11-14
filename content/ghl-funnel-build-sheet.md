# GHL funnel build sheet: 6 landing pages + 2 thank-you pages

Sub-account: **Intrasoft Middle East** (`vhJRhZJvL4LvDBJd7NM0`)

GHL's public API can't create funnels or pages, so build these in **Sites → Funnels**. Each step is one
**Custom JS/HTML** element in a full-width section and row with zero padding. Paste the whole file.

## Funnel 1: `Intrasoft | SAP GROW Fast | E-Book`

| # | Step name | Path | Paste this file | Campaign tag sent |
|---|---|---|---|---|
| 1 | GF V1 · Myths | `/gf-myths` | `landing-pages/variants/grow-fast/v1-myths.html` | `grow-fast-v1-myths` |
| 2 | GF V2 · Clear Answers | `/gf-clear-answers` | `landing-pages/variants/grow-fast/v2-clear-answers.html` | `grow-fast-v2-answers` |
| 3 | GF V3 · Growth | `/gf-growth` | `landing-pages/variants/grow-fast/v3-growth.html` | `grow-fast-v3-growth` |
| 4 | GF · Thank You | `/gf-thank-you` | `landing-pages/thank-you/grow-fast.html` | `grow-fast-thank-you` |

## Funnel 2: `Intrasoft | SAP BDC | E-Book`

| # | Step name | Path | Paste this file | Campaign tag sent |
|---|---|---|---|---|
| 1 | BDC V1 · One Truth | `/bdc-one-truth` | `landing-pages/variants/bdc/v1-one-truth.html` | `bdc-v1-one-truth` |
| 2 | BDC V2 · Reliable AI | `/bdc-reliable-ai` | `landing-pages/variants/bdc/v2-reliable-ai.html` | `bdc-v2-reliable-ai` |
| 3 | BDC V3 · Finance & Operations | `/bdc-finance-ops` | `landing-pages/variants/bdc/v3-finance-operations.html` | `bdc-v3-finance-ops` |
| 3b | BDC V4 · Impactful Decisions (second E-Book, test) | `/bdc-impactful-decisions` | `landing-pages/variants/bdc/v4-impactful-decisions.html` | `bdc-v4-impactful-decisions` |
| 4 | BDC · Thank You | `/bdc-thank-you` | `landing-pages/thank-you/bdc.html` | `bdc-thank-you` |

The landing page files already point to `/gf-thank-you` and `/bdc-thank-you`. Keep those exact paths, and put both
funnels on the same domain as the landing pages, or edit `thankYouUrl` in each file.

**One BDC thank-you page serves both E-Books and both audiences.** The landing page adds a small tag to the link, and the page
switches its E-Book title and step 2 to match. No second thank-you page is needed.

| BDC landing page | `thankYouUrl` | Thank-you page shows |
|---|---|---|
| V1 One truth, V3 Finance ops | `/bdc-thank-you` | Connect and Harmonize + finance planning data review |
| V2 Reliable AI (CIO, data leaders) | `/bdc-thank-you?for=ai` | Connect and Harmonize + **data and AI readiness review** |
| V4 Impactful decisions | `/bdc-thank-you?ebook=impactful` | Driving Impactful Business Decisions (no cover until the team designs one) + finance data review |

Optional: set `bookingUrlAi` in `thank-you/bdc.html` to give the AI review its own calendar. Empty = same calendar.

**Calendar:** the "Intrasoft" calendar must offer **Sunday to Thursday** (Saudi Arabia and Jordan working week), not Friday. In GHL:
Calendars > Intrasoft > Availability, and check the team member's own availability too. Also set the week to start on Sunday
if GHL offers it. Test by opening `/bdc-thank-you`: Friday and Saturday must be greyed out.

**Each step gets its own path.** The full post → page → E-Book mapping is in `content/social-portfolio-review.md`.

## Before publishing each step, fill in `LP_CONFIG`

- `formEndpoint`: the Inbound Webhook URL of that product's workflow (one per product)
- `ebookUrl`: the PDF link (upload the PDF to the Media Library)
- `privacyUrl`, `logoUrl`, `sapLogoUrl`
- Thank-you pages: `bookingUrl` (the GHL calendar), and optionally `contactUrl`

## Already created in GHL via API

**Custom values** (Settings → Custom Values). Fill them in once and every email updates:

| Custom value | Fill with |
|---|---|
| `{{ custom_values.sap_grow_fast_ebook_url }}` | GROW Fast PDF link |
| `{{ custom_values.sap_grow_fast_fit_check_url }}` | `https://<domain>/gf-thank-you#isl-next` or the calendar link |
| `{{ custom_values.sap_bdc_ebook_url }}` | BDC PDF link |
| `{{ custom_values.sap_bdc_data_review_url }}` | `https://<domain>/bdc-thank-you#isl-next` or the calendar link |
| `{{ custom_values.sap_email_sender_name }}` | The Intrasoft sender's name |
| `{{ custom_values.sap_email_sender_title }}` | Their title, e.g. "SAP Cloud ERP Lead, Intrasoft Middle East" |

**12 email templates** (Marketing → Emails → Templates), named `SAP GROW Fast · E0…E5` and `SAP BDC · E0…E5`.
Templates don't store subject lines. Set the subject in each workflow's Send Email action:

| Template | Subject | A/B alternative |
|---|---|---|
| SAP GROW Fast · E0 | Your SAP GROW Fast Myth Busting E-Book | {{contact.first_name}}, here's your copy |
| SAP GROW Fast · E1 | The "too expensive" question | What would SAP really cost a company your size? |
| SAP GROW Fast · E2 | Why ERP projects run over | It's rarely the software |
| SAP GROW Fast · E3 | The month-end test | How many days does your month-end close take? |
| SAP GROW Fast · E4 | Who runs it after go-live? | You don't need an in-house SAP team |
| SAP GROW Fast · E5 | Should you look at this now, or next year? | The real cost of waiting |
| SAP BDC · E0 | Your SAP E-Book: Connect and Harmonize Business Data | {{contact.first_name}}, here's your copy |
| SAP BDC · E1 | Same business. Same question. Different numbers. | Why your reports disagree |
| SAP BDC · E2 | Excel isn't the problem | Relying on it alone is |
| SAP BDC · E3 | "What happens if…?" | The question leadership asks finance most |
| SAP BDC · E4 | Before your AI pilot, check this | Reliable AI starts with reliable data |
| SAP BDC · E0b (V4 only) | Your E-Book: Driving Impactful Business Decisions | {{contact.first_name}}, here's your copy |
| SAP BDC · E5 | The next decision won't wait for the next budget | An honest question about timing |

Workflow timing, tags and exits: see `content/nurture/ghl-workflow-notes.md`.

## Existing funnels to tidy up

- **"1st sap product"** has 3 steps that all use the same path, `/sap-grow-fast`. Only one can be reached.
