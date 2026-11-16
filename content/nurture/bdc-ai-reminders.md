# SAP Business Data Cloud (AI readiness): booking reminders

Sent to anyone who books a data and AI readiness review. Timed before the call starts: 24 hours, 6 hours, 3 hours and 15 minutes.
Merge fields: `{{contact.first_name}}`, `{{appointment.start_time}}`, `{{appointment.reschedule_link}}`.

---

## R0 · On booking · Booking confirmation

**Subject:** Your data and AI readiness review is booked. See you soon
**Alt subject:** {{contact.first_name}}, your readiness review is booked
**Preview:** Your time, your meeting link, and how to reschedule.

Hi {{contact.first_name}},

Thank you for booking your data and AI readiness review. We're looking forward to it.

**When:** {{appointment.start_time}}
**How long:** 30 minutes, online
**With:** an Intrasoft data and analytics consultant

[Join the meeting]({{appointment.meeting_location}})

Save this email: the button above is your meeting link. You'll also get a short reminder before the call.

Need a different time? [Reschedule here]({{appointment.reschedule_link}}).

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R1 · 24 hours before · Your readiness review is tomorrow

**Subject:** {{contact.first_name}}, tomorrow we look at your AI plans together
**Alt subject:** Tomorrow: 30 minutes on your AI plans
**Preview:** Here's what to have ready.

Hi {{contact.first_name}},

Your 30-minute data and AI readiness review is tomorrow, at {{appointment.start_time}}.

To make the most of it, have these ready:

- The AI initiatives you are considering, even if they are early
- The main systems and data sources they would depend on
- Any data quality problems your teams already know about

Need to move the time? [Reschedule here]({{appointment.reschedule_link}}). No need to reply.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R2 · 6 hours before · Your readiness review is today

**Subject:** Today we see how ready your data is for AI
**Alt subject:** See you at {{appointment.start_time}}
**Preview:** A quick reminder for today.

Hi {{contact.first_name}},

Your data and AI readiness review starts today at {{appointment.start_time}}. It takes 30 minutes, and you'll speak with an Intrasoft data and analytics consultant about your own business.

If anything has changed, [reschedule here]({{appointment.reschedule_link}}).

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R3 · 3 hours before · Starting in about 3 hours

**Subject:** A few hours to go. One question to bring
**Alt subject:** One question to bring with you
**Preview:** Think about this before the call.

Hi {{contact.first_name}},

Your review starts at {{appointment.start_time}}. Before you join, think about:

- Which AI use case you would most like to see working in a year
- Whether your teams trust the numbers they use today

No preparation beyond that is needed. We'll work through the rest together.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R4 · 15 minutes before · Your call starts in 15 minutes

**Subject:** We're ready when you are (15 minutes)
**Alt subject:** Join us in 15 minutes
**Preview:** Your meeting link is inside.

Hi {{contact.first_name}},

Your review starts at {{appointment.start_time}}. Join with the button below when you are ready.

[Join the meeting]({{appointment.meeting_location}})

See you soon.

[SENDER NAME]
[TITLE], Intrasoft Middle East

---
