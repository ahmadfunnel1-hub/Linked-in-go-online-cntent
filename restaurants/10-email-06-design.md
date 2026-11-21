# 10 — تصميم إيميل البيع: "باقي يومين على تجربتك" (إيميل 6 من السلسلة)

| البند | القيمة |
|---|---|
| النوع | **Sales Email** (مع Urgency حقيقي: نهاية التجربة) |
| موقعه | يوم 12 من التجربة (`07-email-sequence.md`) |
| الهدف | تفعيل الاشتراك المدفوع ($39) قبل نهاية التجربة — الخوف من خسارة متجر شغال (FOMO حقيقي) |
| الكود | `restaurants/emails/email-06-trial-ending.html` |
| الصور | `restaurants/emails/img/` (SVG المصدر + **PNG جاهز**) |
| الهوية | Primary/CTA `#0F766E` • Secondary `#F2B441` • خلفية الإيميل `#F4F1EA` • بطاقة `#FFFFFF` • نص `#1C1C1A` • ثانوي `#6B6B63` • خطوط: Tahoma/Arial داخل الإيميل (Readex/IBM Plex داخل الصور فقط) |

> ⚠️ **SVG لا يعمل في Gmail وOutlook.** كل عنصر SVG هنا مُحوَّل لـ PNG (بدقة 2x) وهو اللي يُستخدم في الإيميل. الـ SVG للتعديل فقط.
> ⚠️ الخطوط المخصصة لا تُحمّل في أغلب الكلاينتات → النص الحي بـ Tahoma (أفضل خط عربي متاح افتراضياً)، والخطوط الخاصة داخل صورة الهيدر فقط.

---

## الخطوة 1 — Subject + Preview
| # | الأسلوب | Subject | Preview |
|---|---|---|---|
| 1 | نتيجة شخصية | **{{store_name}}: {{orders_count}} طلب بـ 12 يوم** | وباقي يومين على تجربتك — خلّي المتجر يضل شغال. |
| 2 | وضوح/إلحاح | **باقي يومين على تجربتك** | الرابط اللي نشرته بيحتاج اشتراك حتى يضل يستقبل طلبات. |
| 3 | خسارة (FOMO) | **لا توقف متجر صار شغّال** | دقيقة وحدة، ومتجرك بيكمل بدون ما يوقف ولا يوم. |

> لمن `orders_count = 0` استخدم النسخة البديلة من `07` (CTA للمساعدة بدل الدفع) — وإلا الإيميل بيحرج.

## الخطوة 2 — الهيكل
| # | Section | المحتوى | الهدف النفسي | العنصر البصري |
|---|---|---|---|---|
| 1 | Logo bar | الشعار | تعرّف فوري على المرسل | شعار PNG |
| 2 | Header Banner | «باقي يومين • تجربتك قرّبت تخلص» + شريط تقدم 85% | Urgency بصري قبل القراءة | Banner 600×200 |
| 3 | Hook | «{{first_name}}، متجرك اشتغل» | فخر/إنجاز — قبل/بعد | — |
| 4 | Story/Proof | بطاقة «{{orders_count}} طلب» | إثبات شخصي (أقوى من أي شهادة) | أيقونة طابعة + بطاقة خضراء فاتحة |
| 5 | Problem/FOMO | التجربة بتخلص + الرابط والزبائن | ألم الخسارة (Loss aversion) | — |
| 6 | Divider | — | تنفّس قبل الحل | Divider 600×24 |
| 7 | Solution Bridge | «فعّل، والمتجر بيكمل… الإعدادات بتضل» | إزالة احتكاك الانتقال | — |
| 8 | Offer | ستور $39 + ما يشمله + إضافات + مقارنة العمولة | السعر بعد الفائدة | بطاقة بإطار أخضر + Badge زعفراني |
| 9 | CTA | «فعّل اشتراكك — $39 بالشهر» | قرار واحد | زر Bulletproof (يعمل في Outlook) |
| 10 | P.S. | لمن رقمه قليل: انشر الرابط اليوم | معالجة اعتراض "ما جاني طلبات" | — |
| 11 | Footer | سبب الإيميل، الخصوصية، إلغاء الاشتراك، العنوان | ثقة + امتثال | — |

## الخطوة 3 — المحتوى
مكتوب كاملاً داخل ملف الـ HTML (نفس نص إيميل 6 في `07` بعد ضبطه للتصميم). الاستعجال مبني فقط على **نهاية التجربة الحقيقية**.
> ⚠️ جملة «بعد التجربة، المتجر بيحتاج اشتراك حتى يضل يستقبل طلبات» عليها تعليق `[تأكيد مطلوب]` — عدّلها لتطابق ما يحدث فعلاً.

## الخطوة 4 — العناصر البصرية + برومبتات SVG
> الثلاثة **مولّدة وجاهزة** في `emails/img/` (SVG + PNG). البرومبتات للتعديل أو لإعادة التوليد بأداة أخرى.

### 1) Header Banner — 600×200
> Flat SVG email header, width 600 height 200, solid background #0F766E. Two very subtle concentric circle outlines top-right and one bottom-left, stroke #FFFFFF at 8% opacity. Centered pill badge 128×30 rx 15 fill #F2B441 with Arabic text "باقي يومين" (Readex Pro bold 15px, #1C1C1A). Below it Arabic headline "تجربتك قرّبت تخلص" (Readex Pro bold 30px, #FFFFFF, centered, y=112). Subtitle "متجرك شغّال… خلّيه يضل شغّال" (IBM Plex Sans Arabic 17px, #FFFFFF 85% opacity, y=150). Small progress bar at bottom center: track 60×6 rx3 #FFFFFF 25% opacity, fill 51×6 #F2B441 (85%). No gradients, RTL text, export PNG 2x.

### 2) Stat Icon — 48×48
> Flat line icon SVG 48×48, rounded square rx 12 fill #E6F2F0, centered 24px receipt printer with ticket, stroke #0F766E 2px rounded joins, one ticket line in #F2B441. Transparent outside the square.

### 3) Divider — 600×24
> SVG 600×24 transparent: two short lines #E5DED2 1.5px (x 190–278 and 322–410, y 12), three center dots: #0F766E r3 at 288, #F2B441 r4 at 300, #0F766E r3 at 312.

### 4) الشعار
استخدم PNG الشعار الرسمي (ارتفاع 28px، عرض حسب النسبة، خلفية شفافة). لا تولّد شعاراً.

### الزر
**ليس صورة** — زر HTML/VML (Bulletproof) حتى يظهر حتى لو الصور مطفأة.

## الخطوة 5 — الكود
`email-06-trial-ending.html`:
- Table layout 100%، حاوية 600px في الوسط، Inline CSS على كل عنصر.
- RTL (`dir="rtl"` + `text-align:right`).
- Preview text مخفي في أول الـ body.
- زر Bulletproof: VML لـ Outlook + `<a>` لباقي الكلاينتات.
- صور `width:100%;max-width:600px;height:auto` + `alt` نصي + لون خلفية للهيدر (يظهر الكلام حتى لو الصور محجوبة).
- بلوك `<style>` صغير للجوال فقط (تحسين؛ الإيميل لا يعتمد عليه).

## الخطوة 6 — التسليم

### 1. ترتيب الصور
1. **الشعار الرسمي** (PNG)
2. **header.png** (جاهز)
3. **stat-icon.png** (جاهز)
4. **divider.png** (جاهز)

### 2. تركيب الصور
- ارفع الـ PNG على منصة الإيميل (Media Library) أو CDN، وانسخ الرابط العام (https).
- ابحث عن `https://YOUR-CDN/` في الكود واستبدله بالرابط لكل صورة.
- الشعار: استبدل `<span>سينكرو</span>` تحت تعليق `IMG: شعار` بـ:
  `<img src="LOGO_URL" height="28" alt="سينكرو" style="display:block;height:28px;width:auto;border:0;">`

### 3. النسخ في المنصة
**GoHighLevel (الأساسي):**
1. Marketing → Emails → Templates → New → **Code Editor (HTML)**.
2. الصق الكود كاملاً.
3. بدّل المتغيرات: `{{first_name}}`→`{{contact.first_name}}`، و`{{store_name}}`/`{{orders_count}}`/`{{trial_end_date}}`/`{{billing_link}}` → **Custom Fields** في GHL (أنشئها: `contact.store_name`، `contact.orders_count`، …) تُحدَّث من Webhook سينكرو.
4. `{{unsubscribe_link}}` → رابط الإلغاء الخاص بـ GHL (`{{email.unsubscribe_link}}` أو الفوتر التلقائي)، و`{{company_address}}` → عنوان الشركة.
5. ضع القالب في الـ Workflow يوم 12 مع شرط `subscribed = false`.

**Mailchimp:** Create → Email → Code your own → Paste in code. المتغيرات بصيغة `*|FNAME|*` و`*|UNSUB|*`.
**ActiveCampaign:** Campaign/Automation → Custom HTML. المتغيرات `%FIRSTNAME%` و`%UNSUBSCRIBELINK%`.

### 4. تعديلات بعد النسخ
- [ ] أكواد الألوان الرسمية لسينكرو (ابحث عن `#0F766E` واستبدل) + أعد تصدير PNG.
- [ ] تأكيد جملة نهاية التجربة.
- [ ] رابط الدفع الصحيح.
- [ ] Send test لـ Gmail (ويب + جوال)، Outlook، Apple Mail — وجرّب مع **إيقاف الصور**.
- [ ] Subject A/B: #1 ضد #2.
- [ ] اعتماد Muhammad.
