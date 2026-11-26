# Abu AlKhair – Conversation AI agent review (Nov 1–16, 2026)

Agent: "Restaurant and cafe agent" (yv6ELc4GkJ2KuZ1kVR3f). 1,066 AI replies, 171 handoff-style replies, 165 customers.

## What the handoffs really are

| Cause | Count | Fix |
|---|---|---|
| English "Got it, I'll get back to you shortly." sent after an emoji / reaction / "." | 145 | Platform fallback, not the prompt (see A) |
| Same reply after WhatsApp voice-call events / voice notes | 18 | Same as above |
| Same reply after reactions to videos | 4 | Same as above |
| Same reply after real text ("منيو", a joke) | 4 | Prompt/setting |
| "منطقتك بحاجة تأكيد" (delivery area not in table) | ~19 | Add areas to knowledge base (B) |
| "هاد التفصيل بده تأكيد مباشر" – real questions | ~63 distinct | Knowledge base + small prompt rules (C, D) |

## A. The English "Got it..." message (biggest issue, 64% of handoffs)
- The prompt says: ignore emojis, reactions and system events, reply in Arabic only. The agent can't send "nothing", so GHL sends its default English text instead.
- Prompt text can't fully fix this. Check the agent's settings in GHL (Actions: `transferBot`, `advancedFollowup`; and the default/fallback message) and change the fallback message to Arabic or disable it.
- If it can't be disabled: add a rule giving a short Arabic reply for emoji-only messages (suggestion below) instead of silence.

Suggested replacement for rule 16 (last bullet):
> إذا وصل إيموجي أو تفاعل منفرد ولا يمكن تجاهله، لا ترسل أي نص إنجليزي أبداً. إن لزم الرد، استخدم: «تسلم، بنتشرف فيك دايماً.»

## B. Delivery areas missing from the knowledge-base table
Asked and not found: طبربور, الجبيهة, البنيات, أبو علياء, عمان (generic), إربد, جرش (partly), منارة, عين الباشا.
Action (owner): send the delivery price for each area, and I'll add them to the knowledge base.

## C. Knowledge-base gaps (owner to confirm – I won't invent these)
1. How many tripe (كرشات) pieces in a quarter kilo; how many people a quarter/half kilo serves.
2. What comes with a whole head (راس): does it include the brain (مخ/نخاع)? Price of the portable "راس سفري" and what comes with it.
3. Cooked vs raw (مسلوق / مشوي / مطبوخ / "بلا جميد") – what's available and any price difference.
4. Packaging: can each half kilo come in a separate box?
5. Group meals / offers for 3–4 people ("وجبة الأصحاب", "عروض ٣ أشخاص", "وجبة الأكيل") – what's included and prices.
6. Add-on prices (e.g. laban, soup) and prices of fatteh items.
7. How long an order takes to prepare; order cut-off hour; pickup times.
8. Vegetarian options.
9. Photos: can the agent send dish photos? (several customers asked)

## D. Prompt additions (add after section 10, Delivery)

**Location pin / map link:**
> إذا أرسل الزبون لوكيشن أو رابط خريطة بدل اسم المنطقة، اسأله عن اسم المنطقة أو الحي بجملة واحدة، ولا تحوّله للهاتف مباشرة.

**Customers who can't call:**
> إذا قال الزبون إنه ما بقدر يتصل (ما معه رصيد أو بحكي واتساب بس)، لا تكرر طلب الاتصال. [OWNER: confirm whether 0796222302 accepts WhatsApp messages. If yes:] «تقدر تراسلنا واتساب على نفس الرقم 0796222302.»

**Orders:** many customers write "بدي أطلب" and then never call. After the order total (section 11), add:
> إذا قال الزبون إنه ما بقدر يتصل، أعطه خيار المراسلة على واتساب على نفس الرقم بدل تكرار طلب الاتصال. [only if confirmed]

**Short unclear messages** ("." / ".." / "؟"):
> الرسائل التي تحتوي نقطة أو علامة استفهام فقط تُعامل كتفاعل منفرد وتتبع قاعدة التفاعلات.

## E. Things I did NOT change
- Nothing has been changed in GHL for this review. The prompt in GHL is unchanged.
- The current prompt is well structured; I'd add to it, not rewrite it.
