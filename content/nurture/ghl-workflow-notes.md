# GHL build notes: thank-you pages and nurture sequences

Build it in this order, as a checklist. Do it once per product (GROW Fast, BDC).

## 1. Pages (funnel steps)

| Step | GROW Fast | BDC |
|---|---|---|
| Landing page | `sap-2` (or a version from `landing-pages/variants/grow-fast/`) | `sap-1` (or a version from `landing-pages/variants/bdc/`) |
| Thank-you page | new step, e.g. `sap-2-thank-you`: paste `landing-pages/thank-you/grow-fast.html` | new step, e.g. `sap-1-thank-you`: paste `landing-pages/thank-you/bdc.html` |

- On each **landing page**, set `thankYouUrl` in `LP_CONFIG` to that product's thank-you page link.
- On each **thank-you page**, set `ebookUrl`, `bookingUrl` (the GHL calendar link), and optionally `contactUrl` (WhatsApp or email) and `logoUrl`/`sapLogoUrl`.
- The landing page passes only the **first name** to the thank-you page, held in the browser tab (sessionStorage), never in the URL.

## 2. Calendars

- One calendar per product, 30 minutes: **GROW Fast fit check** and **Finance planning data review**.
- Assign the Intrasoft consultants (round robin if more than one).
- Availability: **Sunday to Thursday**, Saudi working hours (Asia/Riyadh).
- Turn off GHL's own confirmation emails if the workflow below sends them, so nobody gets duplicates.

## 3. Tags

| Tag | Added when |
|---|---|
| `grow-fast-mythbusting` / `bdc-finance-planning` (or the variant's `campaign` value) | Form submitted |
| `ebook-download` | Form submitted |
| `marketing-consent` | Form submitted with `marketingConsent = true` |
| `fit-check-booked` / `data-review-booked` | Appointment booked |
| `nurture-replied` | Contact replies to any nurture email |
| `nurture-later` | Contact replies "later" |

## 4. Workflows

**Workflow 1: E-book delivery and nurture (one per product)**
- **Trigger:** Inbound Webhook or form submitted, from that product's landing page.
- **Actions:**
  1. Create/update contact. Map the fields and add tags (see the README).
  2. **Send E0** (the delivery email) to everyone, immediately.
  3. Internal notification to the assigned consultant: "New e-book lead: {{contact.name}}, {{contact.company_name}}, {{contact.job_title}}".
  4. **If/Else:** `marketing-consent` tag present?
     - **No:** end. They received only the e-book.
     - **Yes:** E1 (wait 2 days) → E2 (wait 2 days) → E3 (wait 3 days) → E4 (wait 3 days) → E5 (wait 4 days).
- **Send window:** Sunday to Thursday, 09:00–11:00 Asia/Riyadh. No Friday sends.
- **Goal / exit:** appointment booked, OR tag `nurture-replied`, OR unsubscribed. They leave the sequence immediately.
- **Re-entry:** off. A contact who downloads twice doesn't get the sequence twice.

**Workflow 2: Booking**
- **Trigger:** appointment booked on the product calendar.
- **Actions:** add the `…-booked` tag, move the opportunity to "Call booked", send a confirmation and a reminder 24 hours before and 1 hour before.

**Workflow 3: Replies**
- **Trigger:** customer replied (email).
- **Actions:** add `nurture-replied` (stops Workflow 1) and create a task for the consultant to answer within 1 business day. If the reply is "later", add `nurture-later` and a task for 90 days.

## 5. Pipeline: "SAP leads"

E-book downloaded → Engaged (clicked a nurture link) → Call booked → Call held → Proposal → Won / Lost

## 6. Speed to lead

When the job title contains CEO, CFO, CIO, Director or Head, create a task for the consultant to reach out personally within **4 business hours**. Senior downloaders are the warmest leads.

## 7. Compliance (Saudi PDPL)

- E1–E5 go only to contacts who ticked the optional marketing box. The rest get E0 only.
- Every marketing email has an unsubscribe link (GHL adds it by default; don't remove it).
- Keep the stored consent text and timestamp (`marketingConsentText`, `submittedAt`) on the contact.

## 8. KPIs (weekly)

Landing page conversion rate → e-book downloads → nurture click rate → **calls booked** → calls held → proposals.
Compare landing page versions by the `campaign` tag.
