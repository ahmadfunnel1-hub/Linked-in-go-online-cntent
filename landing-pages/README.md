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
- `ebookUrl`: the hosted URL of the approved e-book PDF. It opens after a successful submit and is linked on the thank-you state.
- `privacyUrl`: your privacy notice.

## What's built in

- The 5-field form from the brief: full name, business email (free-mail domains rejected), company, job title, company size.
- Optional, unticked marketing consent. The download doesn't depend on it.
- UTM capture, and `dataLayer` events: `page_view`, `ebook_cta_click`, `form_start`, `form_error`,
  `form_submit_success`, `thank_you_view`, `resource_download_success`.
- Responsive layout down to phone width.

## Still to replace (approval gates from the brief)

- **GROW Fast proof section (`#proof`)**: the dashed cards and quote are placeholders. Fill them with verified
  SAP partner status, regional delivery facts and an approved testimonial, or delete any slot you can't fill.
  Don't launch with bracketed text.
- **E-book title**: the GROW Fast page uses "SAP GROW Fast Myth Busting E-Book", taken from the SAP asset
  `SAP_GROW_Fast_Myth_Busting_E-Book.pdf`. Use the same title in the delivery email and CRM.

- The logo slots and e-book covers are placeholders. Use approved SAP and Intrasoft assets.
- The colours are neutral placeholders in the `:root` tokens. Apply the official brand guides.
- Confirm the GROW Fast scope, pricing wording and the ~4-month target with Intrasoft.
- Confirm which BDC/SAC services Intrasoft offers before adding proof or case studies.
