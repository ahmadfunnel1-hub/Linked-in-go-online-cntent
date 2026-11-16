# Direct bookings: neutral reminders

Sent to anyone who books through the general "Book a call" page. Timed before the call starts: 24 hours, 6 hours, 3 hours and 15 minutes.
Merge fields: `{{contact.first_name}}`, `{{appointment.start_time}}`, `{{appointment.reschedule_link}}`.

---

## R0 · On booking · Booking confirmation

**Subject:** Your call with Intrasoft is booked. See you soon
**Alt subject:** {{contact.first_name}}, your call with Intrasoft is booked
**Preview:** Your time, your meeting link, and how to reschedule.

Hi {{contact.first_name}},

Thank you for booking your call with Intrasoft. We're looking forward to it.

**When:** {{appointment.start_time}}
**How long:** 30 minutes, online
**With:** an Intrasoft SAP consultant

[Join the meeting]({{appointment.meeting_location}})

Save this email: the button above is your meeting link. You'll also get a short reminder before the call.

Need a different time? [Reschedule here]({{appointment.reschedule_link}}).

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R1 · 24 hours before · Your data review is tomorrow

**Subject:** {{contact.first_name}}, we're looking forward to tomorrow
**Alt subject:** Tomorrow: 30 minutes on your business
**Preview:** Here's what to have ready.

Hi {{contact.first_name}},

Your 30-minute call with Intrasoft is tomorrow, at {{appointment.start_time}}.

To make the most of it, have these ready:

- The systems and spreadsheets your teams use today
- The process, report or decision that takes the most effort
- Your timeline, if you have one

Need to move the time? [Reschedule here]({{appointment.reschedule_link}}). No need to reply.

Thank you,
[SENDER NAME]
[TITLE], Intrasoft Middle East

---

## R2 · 6 hours before · Your data review is today

**Subject:** Today's the day: your call with Intrasoft
**Alt subject:** See you at {{appointment.start_time}}
**Preview:** A quick reminder for today.

Hi {{contact.first_name}},

Your call with Intrasoft starts today at {{appointment.start_time}}. It takes 30 minutes, and you'll speak with an Intrasoft SAP consultant about your own business.

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

Your call starts at {{appointment.start_time}}. Before you join, think about:

- The one question you most want answered
- What a good outcome from the call would look like for you

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

Your call starts at {{appointment.start_time}}. Join with the button below when you are ready.

[Join the meeting]({{appointment.meeting_location}})

See you soon.

[SENDER NAME]
[TITLE], Intrasoft Middle East

---
