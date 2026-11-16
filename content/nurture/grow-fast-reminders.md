# SAP GROW Fast: booking reminders

Sent to anyone who books a fit check. Timed before the call starts: 24 hours, 6 hours, 3 hours and 15 minutes.
Merge fields: `{{contact.first_name}}`, `{{appointment.start_time}}`, `{{appointment.reschedule_link}}`.

---

## R1 · 24 hours before · Your fit check is tomorrow

**Subject:** Your GROW Fast fit check is tomorrow
**Alt subject:** Tomorrow: 30 minutes on your SAP plan
**Preview:** Here's what to have ready.

Hi {{contact.first_name}},

Your 30-minute GROW Fast fit check is tomorrow, at {{appointment.start_time}}.

To make the most of it, have these ready:

- Your current systems, or the spreadsheets you use for finance, sales and stock
- The decision or report that causes the most trouble today
- Your rough timeline, if you have one

Need to move the time? [Reschedule here]({{appointment.reschedule_link}}). No need to reply.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R2 · 6 hours before · Your fit check is today

**Subject:** Your GROW Fast fit check is today
**Alt subject:** See you at {{appointment.start_time}}
**Preview:** A quick reminder for today.

Hi {{contact.first_name}},

Your GROW Fast fit check starts today at {{appointment.start_time}}. It takes 30 minutes, and you'll speak with an Intrasoft SAP consultant about your own business.

If anything has changed, [reschedule here]({{appointment.reschedule_link}}).

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R3 · 3 hours before · Starting in about 3 hours

**Subject:** Your GROW Fast fit check starts in 3 hours
**Alt subject:** A few questions to have ready
**Preview:** Three things to think about before the call.

Hi {{contact.first_name}},

Your fit check starts at {{appointment.start_time}}. Before you join, think about:

- Which part of your SAP plans you most want to clear up
- Your biggest worry about cost, time or complexity
- Who else in your team should be involved later

No preparation beyond that is needed. Anything you don't know yet, we'll work through together.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R4 · 15 minutes before · Your call starts in 15 minutes

**Subject:** Your GROW Fast fit check starts in 15 minutes
**Alt subject:** Join us in 15 minutes
**Preview:** Use the link in your calendar invitation.

Hi {{contact.first_name}},

Your fit check starts at {{appointment.start_time}}. Please join using the link in your calendar invitation.

See you soon.

[SENDER NAME]
[TITLE], Intrasoft Middle East

---
