# Intrasoft SAP landing pages

Two lead-generation pages, one per product, built from the brief in
`content/Intrasoft_Complete_Conversation_and_Landing_Page_Archive.docx`.

| Page | File | Live URL (GHL) | Audience | Lead magnet |
|---|---|---|---|---|
| SAP Cloud ERP – GROW Fast | `grow-fast/index.html` | https://menu.goonlinejo.com/sap-2 | CEO, CFO, CIO at growing mid-size manufacturers in Saudi Arabia | SAP GROW Fast Myth Busting e-book |
| SAP Business Data Cloud (finance planning with SAP Analytics Cloud) | `bdc/index.html` | https://menu.goonlinejo.com/sap-1 | CFO, Finance Director, FP&A leaders | Connect and Harmonize Business Data e-book |

Each page is a single self-contained HTML file. It works as a standalone page, or you can paste it into GoHighLevel.

## Pasting into GoHighLevel

1. Open the file, select everything (Ctrl/Cmd+A) and copy it.
2. In the GHL page builder, add a full-width section with one full-width row and zero padding. Add a
   **Custom JS/HTML** element and paste the whole file into it.
3. Edit `LP_CONFIG` (near the top of the file) before pasting, or inside the GHL element afterwards.
4. Preview and publish. Use one page per GHL funnel step: GROW Fast and BDC each get their own step.

Every class and ID is prefixed `isl-` and all CSS is scoped under `.isl-lp`, so the page can't change
GHL's own styles, and GHL's theme can't change the page. Duplicate IDs (such as a GHL form field with
`id="email"`) don't conflict either. In-page buttons scroll smoothly without changing the URL.

## Before launch, set `window.LP_CONFIG` in each file

- `formEndpoint`: the URL that receives leads as JSON (CRM or GHL webhook). If it's empty, the form validates but sends nothing.
- `ebookUrl`: the hosted URL of the approved e-book PDF. A tab opens on submit and loads it once the lead is saved; the thank-you screen also has a download button.
- `ebookCoverUrl` (GROW Fast; the BDC hero shows a scenario visual instead): the official SAP e-book cover image. Put it in `<page>/assets/` and use e.g. `"assets/ebook-cover.png"`. If it's empty, a text mock-up is shown, which isn't for production.
- `privacyUrl`: your privacy notice.

### Connecting the form to a GoHighLevel sub-account

Use one workflow per page so each page gets its own tag and follow-up.

1. In the sub-account, go to **Automation → Workflows → Create workflow → Start from scratch**.
2. Add the trigger **Inbound Webhook** and copy its URL (`https://services.leadconnectorhq.com/hooks/...`).
3. Paste that URL into `formEndpoint` in the page's `LP_CONFIG` and republish the page. Leave `formMode: "auto"`:
   it detects the GHL URL and sends form-encoded data, which browsers can post to GHL without being blocked.
4. Submit the form once with test details. In the trigger, click **Fetch sample requests** and pick it, so the
   fields below become available for mapping.
5. Add the action **Create Contact** (or **Create/Update Contact**) and map:
   `fullName` → Full Name, `email` → Email, `company` → Company Name, `jobTitle` and `companySize` → custom fields.
6. Add the page's `campaign` value as a tag: `grow-fast-mythbusting` (plus `ebook-download`) or `bdc-finance-planning` (plus `ebook-download`).
7. Save `marketingConsent`, `marketingConsentText` and `submittedAt` to their own custom fields. Use an **If/Else**
   on `marketingConsent` = `true` before any marketing email or SMS. The e-book delivery email goes to everyone, on both pages.
8. Optionally add **Create Opportunity** in your sales pipeline, then publish the workflow.

Inbound Webhook may be billed as a premium workflow trigger, depending on your GHL plan.

### Lead payload sent to `formEndpoint`

`fullName`, `email`, `company`, `jobTitle`, `companySize`, `marketingConsent` (true/false),
`marketingConsentText` (the exact wording the person agreed to; empty if not ticked), `privacyNoticeUrl`,
`submittedAt` (ISO time), `campaign`, `page`, plus any `utm_*` values. Map `marketingConsent` to its own
CRM field, separate from the lead itself.

## What's built in

- The 5-field form from the brief: full name, business email (free-mail domains rejected), company, job title, company size.
- Optional, unticked marketing consent. The download doesn't depend on it.
- UTM capture, and `dataLayer` events: `page_view`, `ebook_cta_click`, `form_start`, `form_error`,
  `form_submit_success`, `thank_you_view`, `resource_download_success`.
- Responsive layout down to phone width.

## Still to replace (approval gates from the brief)

- Official SAP e-book covers: set `ebookCoverUrl` (see above). The GROW Fast cover is inside
  `SAP_GROW_Fast_Mythbusting-Campaign-2026.zip` → `1_SAP_GROW_Fast_Mythbusting_Campaign_E-Book/SAP_GROW_Fast_Myth_Busting_E-Book.pdf` (page 1).
- The logo slots are placeholders. Use approved SAP and Intrasoft assets.
- The colours are neutral placeholders in the `:root` tokens. Apply the official brand guides.
- E-book title: the GROW Fast page uses "SAP GROW Fast Myth Busting E-Book". If the cover shows a different
  title, update the page to match, and use the same title in the delivery email and CRM.
- Proof: the GROW Fast "Why work with Intrasoft?" section lists confirmed capabilities only. Add a
  verified SAP partner level, delivery numbers or an approved testimonial there when available. Never add an unapproved one.

- Target market is Saudi Arabia only. Have the privacy notice and consent wording reviewed against the
  Saudi Personal Data Protection Law (PDPL).

## Thank-you pages and follow-up

- `thank-you/grow-fast.html` and `thank-you/bdc.html`: confirm the download and invite a free 30-minute call
  (GROW Fast fit check / finance planning data review). Settings: `bookingUrl` (GHL calendar), `contactUrl`. They don't offer the e-book again: the landing page already delivers it.
- Every landing page has `thankYouUrl` in `LP_CONFIG`. Set it to send people to the thank-you page after the form.
- Nurture emails and GHL workflow steps: `content/nurture/`.
- Inputs requested from Intrasoft: `content/intrasoft-request-email.md`.

## Brand-aligned variants (`variants/`)

Three versions per product in the Intrasoft social identity (navy #132146, Intrasoft blue #00A7E3,
light blue #78DCFF, red accent #CD0000). Each hero matches a social post, so ad and page say the same thing.
Every version has its own `campaign` value, so GHL shows which one converts best.

| File | Matches post | Hero style | Body |
|---|---|---|---|
| `variants/grow-fast/v1-myths.html` | GROW Fast Post 01 "Too expensive? Too complex? Too slow?" | Dark | GROW Fast |
| `variants/grow-fast/v2-clear-answers.html` | Posts 02 / 05 / 07 | Light | GROW Fast |
| `variants/grow-fast/v3-growth.html` | Posts 03 / 06 | Dark | GROW Fast |
| `variants/bdc/v1-one-truth.html` | BDC Post 06 + Carousel 4 | Light | Finance planning |
| `variants/bdc/v2-reliable-ai.html` | BDC Posts 04 / 05 + Carousel 2 | Dark | Data & AI |
| `variants/bdc/v3-finance-operations.html` | BDC Post 01 | Dark | Finance planning |

New `LP_CONFIG` options: `logoUrl`, `sapLogoUrl` (approved logo files) and `heroImageUrl`
(reuse a post's artwork behind the hero).

## SAP partner rules applied (client feedback, Nov 8)

- Header: Intrasoft logo only. Hero: Intrasoft logo + SAP Gold Partner logo side by side, separate (no divider),
  SAP logo 96px wide (min 92), never larger than the Intrasoft logo, clear space 32px (half its height = 28px).
- The SAP Gold Partner logo links to https://www.sap.com/partners/profile/intrasoft-middle-east
- Footer uses SAP's trademark statement word for word.
- Page paths must not contain "sap" (otherwise SAP requires "This site is not affiliated with SAP SE or an SAP affiliate
  company."). The new paths (`/gf-…`, `/bdc-…`) are fine. Retire the old `/sap-1` and `/sap-2` pages.
- "E-Book" spelling everywhere. "SAP Gold Partner" in copy. No "Official SAP" or "INTRASOFT × SAP" lines.
- Intrasoft logo: **interim** files cut from the approved covers (`content/brand/logo/`). Replace `logoUrl` /
  `logoOnLightUrl` in `LP_CONFIG` with the official files when Intrasoft sends them.
- To verify with the E-Book PDF: "PureTech Scientific went live in 15 weeks" (quoted as an SAP customer result).

## Headline tests (run one at a time with a GHL split test)

| Page | A (live) | B | C |
|---|---|---|---|
| GROW Fast | Think SAP is too expensive, too slow or too big for your company? Read this first. | Map a faster path to cloud ERP with SAP GROW Fast. (SAP campaign line as the headline) | The 5 SAP myths that keep growing companies stuck on spreadsheets |
| BDC | When business conditions change, can your financial plan keep up? | Your forecast is only as fast as your data. Here's how to fix that. | Why finance teams can't plan fast on disconnected data |

Test the headline first, then the button text ("Send me the free e-book" vs "Get instant access").
Confirm that the "Inside the e-book" bullets match the actual PDFs before launch.

## Business Data Cloud page: sign-off

| Item | Where | Confirm with |
|---|---|---|
| "Plan for What's Next." is a proposed Intrasoft campaign line, not an official SAP tagline | Hero; final CTA | Intrasoft brand / SAP partner guidelines |
| Four service components: planning design, SAC implementation, enablement, managed services | Hero; "What you get" | Intrasoft SAC practice lead |
| Five stages, including "Implement with SAP Activate" | "Why Intrasoft is different" | Intrasoft methodology owner |
| Managed services and optimization are offered as ongoing services | "What you get"; FAQ | Intrasoft commercial |
| Testimonial or case study slot (HTML comment only, nothing shown) | "Building confidence" | Add only with client approval |

## GROW Fast claims to sign off

| Claim on page | Where | Confirm with |
|---|---|---|
| Target of about 4 months to go-live, with a qualifier | "Why Intrasoft GROW Fast" timeline bar; FAQ; myth card | Intrasoft delivery lead |
| Fixed fee for the agreed, predefined scope, separate from the SAP subscription; extras quoted separately | Hero bullet; myth card; pricing card; FAQ | Intrasoft commercial / legal |
| Starting scope covers core finance, supply chain and HR | Manufacturing section; FAQ | Intrasoft GROW Fast package definition |
| Example process flow (purchase order through to reporting) | Manufacturing section | Intrasoft package definition |
| Five phases: Align and define, Configure to proven practices, Validate and prepare, Launch and enable, Support and expand | "How GROW Fast works" | Intrasoft methodology owner |
| Data preparation, agreed data responsibilities and readiness checks are part of the plan | FAQ | Intrasoft delivery lead |
| Fit gaps and out-of-scope requirements are identified before the customer commits | Manufacturing section; FAQ | Intrasoft presales |
| User training is part of the package | Hero; FAQ; "Why work with Intrasoft?" | Intrasoft package definition |
| Six myth/reality answers (from the Offer DNA "myths this offer rejects") | Myth busting section | SAP myth-busting e-book and campaign landing-page copy |
| SAP runs infrastructure, updates, security, maintenance | Benefits; myth card; FAQ | SAP Cloud ERP public edition terms |
| Focus on mid-size manufacturers in Saudi Arabia | Hero note; "Why work with Intrasoft?" | Intrasoft |
