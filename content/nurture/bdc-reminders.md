# SAP Business Data Cloud: booking reminders

Sent to anyone who books a finance planning data review. Timed before the call starts: 24 hours, 6 hours, 3 hours and 15 minutes.
Merge fields: `{{contact.first_name}}`, `{{appointment.start_time}}`, `{{appointment.reschedule_link}}`.

---

## R0 · On booking · Booking confirmation

**Subject:** Your finance planning data review is booked. See you soon
**Alt subject:** {{contact.first_name}}, your data review is booked
**Preview:** Your time, your meeting link, and how to reschedule.

Hi {{contact.first_name}},

Thank you for booking your finance planning data review. We're looking forward to it.

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

## R1 · 24 hours before · Your data review is tomorrow

**Subject:** {{contact.first_name}}, tomorrow we look at your numbers together
**Alt subject:** Tomorrow: 30 minutes on your planning and reporting
**Preview:** Here's what to have ready.

Hi {{contact.first_name}},

Your 30-minute finance planning data review is tomorrow, at {{appointment.start_time}}.

To make the most of it, have these ready:

- The report or forecast that takes the longest to prepare today
- The systems and spreadsheets that feed it
- Any definitions your teams argue about, such as revenue or cost centres

Need to move the time? [Reschedule here]({{appointment.reschedule_link}}). No need to reply.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R2 · 6 hours before · Your data review is today

**Subject:** Today we find where your planning slows down
**Alt subject:** See you at {{appointment.start_time}}
**Preview:** A quick reminder for today.

Hi {{contact.first_name}},

Your finance planning data review starts today at {{appointment.start_time}}. It takes 30 minutes, and you'll speak with an Intrasoft data and analytics consultant about your own business.

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

Your data review starts at {{appointment.start_time}}. Before you join, think about:

- Where your planning slows down between the data and the forecast leadership sees
- Which decision you would make faster with reliable numbers

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

Your data review starts at {{appointment.start_time}}. Join with the button below when you are ready.

[Join the meeting]({{appointment.meeting_location}})

See you soon.

[SENDER NAME]
[TITLE], Intrasoft Middle East

---
