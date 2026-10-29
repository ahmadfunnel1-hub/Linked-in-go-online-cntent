# Intrasoft SAP landing pages

Two separate lead-generation pages built from the brief in
`content/Intrasoft_Complete_Conversation_and_Landing_Page_Archive.docx`.

| Page | File | Audience | Lead magnet |
|---|---|---|---|
| SAP Cloud ERP – GROW Fast | `grow-fast/index.html` | CEO, CFO, CIO at growing mid-size manufacturers (KSA, Oman, Iraq) | SAP GROW Fast Myth Busting e-book |
| SAP Business Data Cloud | `bdc/index.html` | CIO, CDO, data leaders; CFO secondary | Connect and Harmonize Business Data to Amplify the Power of AI |

Each page is a single self-contained HTML file: open it in a browser, or paste it into a
GoHighLevel / CMS custom-code block.

## Before launch, set `window.LP_CONFIG` in each file

- `formEndpoint`: the URL that receives leads as JSON (CRM or GHL webhook). If it's empty, the form validates but sends nothing.
- `ebookUrl`: the hosted URL of the approved e-book PDF. A tab opens on submit and loads it once the lead is saved; the thank-you screen also has a download button.
- `ebookCoverUrl`: the official SAP e-book cover image. Put it in `<page>/assets/` and use e.g. `"assets/ebook-cover.png"`. If it's empty, a text mock-up is shown, which isn't for production.
- `privacyUrl`: your privacy notice.

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

## GROW Fast claims to sign off

| Claim on page | Where | Confirm with |
|---|---|---|
| Target of about 4 months to go-live, with a qualifier | "Why Intrasoft GROW Fast" timeline bar; FAQ; myth card | Intrasoft delivery lead |
| Fixed fee for the agreed, predefined scope, separate from the SAP subscription; extras quoted separately | Hero bullet; myth card; pricing card; FAQ | Intrasoft commercial / legal |
| Starting scope covers core finance, supply chain and HR | Manufacturing section; FAQ | Intrasoft GROW Fast package definition |
| Example process flow (purchase order through to reporting) | Manufacturing section | Intrasoft package definition |
| Five phases: Align, Configure, Validate, Launch, Support | "Why Intrasoft GROW Fast" | Intrasoft methodology owner |
| Six myth/reality answers | Myth busting section | SAP myth-busting e-book and campaign landing-page copy |
| SAP runs infrastructure, updates, security, maintenance | Benefits; myth card; FAQ | SAP Cloud ERP public edition terms |
| Focus on mid-size manufacturers in KSA, Oman, Iraq | Hero note; "Why work with Intrasoft?" | Intrasoft |
