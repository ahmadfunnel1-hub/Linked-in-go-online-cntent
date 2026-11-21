# 09 — تصميم صفحة التسجيل (Opt-in) + برومبتات SVG + التسليم

> الكود الجاهز: **`restaurants/pages/optin.html`** (HTML + CSS + JS للبوب أب في ملف واحد).
> الكوبي من `06`، والفيديو من `08`، والألوان من `04` (سينكرو).
> ⚠️ لم أراجع الصفحات المرجعية (resalatak / coachmaguienehme) في هذا التصميم — الأسلوب مبني على قواعد البراند. أرسلها كصور/لقطات إذا تبي أطابق نمطها.

## الهوية المستخدمة
| الدور | HEX | ملاحظة |
|---|---|---|
| Primary | `#0F766E` | أخضر سينكرو (تقريبي — استبدله بالرسمي في `:root`) |
| Secondary | `#F2B441` | زعفراني للإبراز (خط تحت الكلمات المفتاحية فقط) |
| CTA | `#0F766E` / hover `#0B5B55` | الزر = لون العلامة؛ يبرز لأن الخلفية كريمية |
| Background | `#FBF7F0` | كريمي |
| Surface | `#FFFFFF` | البطاقات |
| داكن (Final CTA) | `#13241C` | |
| Text / Muted | `#1C1C1A` / `#6B6B63` | |
| Fonts | Readex Pro (عناوين) • IBM Plex Sans Arabic (نص) | Google Fonts |

> تغيير كل الألوان = تعديل متغيرات `:root` فقط.

---

## الجزء الأول — البلوكات

| # | البلوك | المحتوى | الهدف النفسي | الخلفية | العنصر البصري |
|---|---|---|---|---|---|
| 0 | Top bar | الشعار فقط | ثقة + لا تشتيت | كريمي | شعار سينكرو (#8) |
| 1 | Eyebrow | «تجربة 14 يوم • بدون بطاقة» | خفض المخاطرة قبل قراءة الوعد | أخضر فاتح (Pill) | أيقونة تشيك صغيرة (#2) |
| 2 | Headline | «خلال أيام، يصير عندك موقع طلبات جاهز… والطلب يطلع على الطابعة لحاله» | نتيجة ملموسة وسريعة | كريمي | إبراز زعفراني تحت «موقع طلبات جاهز» (CSS) |
| 3 | Sub-headline | «فريق سينكرو بيرفع المنيو…» | "مش رح أتعب" | كريمي | — |
| 4 | Flow | موقعك ← الطابعة ← واتسابك | يفهم الآلية في ثانيتين | كريمي | مخطط 3 أيقونات (#1) |
| 5 | CTA #1 + طمأنة | الزر + 3 تطمينات | قرار فوري لمن اقتنع | كريمي | تشيكات صغيرة (#2) + خلفية هيرو (#7) |
| 6 | VSL | فيديو 7 دقائق | إقناع المتردد | داكن داخل إطار أبيض | زر تشغيل (#6) |
| 7 | Divider | — | فصل بصري | كريمي | فاصل (#9) |
| 8 | Benefits | 5 فوائد «رح…» | "هذا بيحل مشكلتي" | أبيض | أيقونات لكل بند (#3a–e) |
| 9 | Highlight box | «ما بدك تدخّل ولا صنف» | إزالة اعتراض الوقت | أخضر | أيقونة "إحنا بنجهّز" (#5) |
| 10 | 3 Steps (إضافة) | سجّل ← بنجهّز ← انشر | السهولة + وضوح ما بعد التسجيل | كريمي | أرقام دائرية (#4a–c) + شريط تقدم (#4) |
| 11 | Trust | 5 شارات حقائق | مصداقية بدون أرقام عملاء | كريمي + بطاقات بيضاء | أيقونات (#10a–e) |
| 12 | Final CTA | الشعار + زر | قرار أخير | داكن `#13241C` | — |
| 13 | Footer | الشروط • الخصوصية | قانوني فقط | كريمي | — |
| — | Popup | 3 حقول + كود دولة | أقل احتكاك | أبيض | — |

---

## الجزء الثاني — العناصر البصرية + برومبتات SVG

> قواعد مشتركة لكل البرومبتات (أضفها في آخر كل برومبت):
> `Flat line icon style, 2px stroke, rounded caps and joins, no gradients, no text unless specified, transparent background, colors only: #0F766E (primary), #F2B441 (accent), #FFFFFF, #1C1C1A. Clean optimized SVG code with viewBox, no embedded raster images, no fonts.`

### #1 — مخطط الآلية (Hero Flow) — الأهم
- **الوصف:** 3 دوائر (64px) أفقياً بينها أسهم منقطة: جوال ← طابعة تخرج تذكرة ← فقاعة محادثة. تحت كل دائرة نص صغير. العرض 520px، في منتصف الهيرو فوق الزر.
- **برومبت:**
> Create an SVG diagram, viewBox 0 0 520 110, RTL reading order (right to left). Three circles (r=32) at x=440, 260, 80, y=40, fill #E6F2F0, stroke #0F766E 2px. Inside right circle: smartphone outline icon with a small cart. Middle circle: receipt printer with a paper ticket coming out (ticket fill #FFFFFF, two #F2B441 lines on it). Left circle: chat bubble icon. Between circles: dashed arrows (stroke #0F766E, dash 4 4) pointing leftwards with rounded arrowheads. Under each circle, Arabic labels in text elements, font-family "Readex Pro", 14px, fill #1C1C1A, text-anchor middle, y=98: "موقعك", "الطابعة", "واتسابك".

### #2 — تشيك صغير (طمأنة/Eyebrow)
- 16px، دائرة أخضر فاتح وعلامة صح خضراء. بجانب كل تطمين.
> SVG icon 16x16 viewBox 0 0 16 16: circle r=8 fill #E6F2F0, checkmark path stroke #0F766E 2px rounded.

### #3a–e — أيقونات الفوائد (44px)
- مربع بزوايا 12px خلفية `#E6F2F0`، الأيقونة بالأخضر، لمسة زعفرانية واحدة.
> Set of 5 SVG icons, each 44x44 viewBox 0 0 44 44, rounded square background rx=12 fill #E6F2F0, icon centered 24px, stroke #0F766E 2px, one small accent detail in #F2B441:
> (a) link chain with a tiny shop awning; (b) receipt printer with ticket, accent on ticket; (c) POS terminal / handheld cashier device with screen accent; (d) person silhouette with circular return arrow, accent on arrow head; (e) target with arrow hitting center, accent on center dot.

### #4 / #4a–c — شريط التقدم + أرقام الخطوات
> (Progress) SVG viewBox 0 0 560 28: horizontal line y=14 stroke #E5DED2 3px from x=40 to 520; three circles r=10 at x=520, 280, 40 fill #0F766E; segment from 520 to 280 stroke #0F766E 3px; segment 280→40 dashed #0F766E. RTL order.
> (Numbers) Three SVGs 56x56: circle r=26 fill #0F766E, inner ring r=22 stroke #F2B441 1.5px, centered numeral "1"/"2"/"3" font-family "Readex Pro" bold 24px fill #FFFFFF.

### #5 — أيقونة "إحنا بنجهّز" (Highlight Box)
> SVG 52x52: open hand holding a menu card, stroke #FFFFFF 2px, menu lines in #F2B441, on transparent background (box is green).

### #6 — زر التشغيل (Video)
> SVG 84x84: circle r=40 fill #0F766E with 4px #FFFFFF ring at 30% opacity; centered play triangle fill #FFFFFF with rounded corners, optically shifted right by 3px.

### #7 — خلفية الهيرو (اختياري)
> Decorative SVG viewBox 0 0 1440 600, preserveAspectRatio xMidYMid slice: two large concentric circular arcs (loop shapes) in #0F766E at 6% opacity stroke 2px, top-right and bottom-left; 6 small dots #F2B441 at 40% opacity scattered. No fill areas. Very subtle.

### #8 — الشعار
- **استخدم الشعار الرسمي من ملف البراند.** لا تولّد شعاراً جديداً.

### #9 — الفاصل
> SVG 220x24: two horizontal lines (#E5DED2, 1.5px) left and right with three dots in center (middle dot #F2B441 r=4, side dots #0F766E r=3).

### #10a–e — أيقونات شارات الثقة (40px)
> Five SVG icons 40x40, line style stroke #0F766E 2px, no background: (a) receipt printer; (b) chat bubble with check; (c) bar chart with up arrow; (d) credit card with diagonal strike line in #F2B441; (e) wrench + gear with "0" feel (no text).

### عناصر احترافية إضافية (موجودة في الكود)
| العنصر | الوصف | تنفيذ |
|---|---|---|
| Eyebrow Pill | «تجربة 14 يوم • بدون بطاقة» فوق العنوان | CSS + #2 |
| Highlight تحت الكلمات | خط زعفراني شفاف تحت الكلمة المفتاحية | CSS (`.hl`) |
| Progress Indicator | 3 خطوات | #4 |
| Highlight Box | اعتراض الوقت | #5 |
| إطار فيديو بظل | Device-like frame | CSS |
| Trust Badges | 5 حقائق | #10 |
| Divider | بين الفيديو والفوائد | #9 |
| Focus states + Esc لإغلاق البوب أب | وصولية | JS/CSS |

---

## الجزء الثالث — الكود
الملف: `restaurants/pages/optin.html` — جاهز للنسخ. يتضمن:
- RTL كامل، Responsive (ديسكتوب / تابلت ≤820px / جوال ≤480px).
- زرين CTA يفتحان نفس البوب أب، إغلاق بـ × أو Esc أو الضغط خارج النافذة.
- حقل الهاتف مع اختيار كود الدولة (الأردن افتراضي — بدّله حسب IP).
- Placeholders واضحة: `<!-- SVG #n: ... -->` بجانب `div` بحجم ثابت.
- مكان تتبع Meta/GA4 عند **الإرسال** فقط.

---

## الجزء الرابع — خطوات التسليم

### 1. ترتيب توليد الـ SVG (الأهم أولاً)
1. **#8 الشعار الرسمي** (من ملف البراند)
2. **#1 مخطط الآلية** — يشرح المنتج فوق الطي
3. **#3a–e أيقونات الفوائد**
4. **#2 التشيك الصغير**
5. **#6 زر التشغيل** (أو احذفه إذا الفيديو iframe جاهز)
6. **#4 / #4a–c التقدم والأرقام**
7. **#10a–e شارات الثقة**
8. **#5 أيقونة Highlight**
9. **#9 الفاصل**
10. **#7 خلفية الهيرو** (اختياري)

### 2. طريقة التركيب
- ابحث في الكود عن `<!-- SVG #رقم` .
- **إذا بعده `<div class="..." aria-hidden="true"></div>`:** استبدل الـ `div` كاملاً بكود الـ `<svg>` وأضف له نفس الـ class (مثلاً `<svg class="ic" ...>`). الـ CSS يضبط الحجم تلقائياً.
- **#2 داخل `.reassure`:** ضع `<svg class="ic" ...>` قبل النص داخل `<span>`.
- **#7:** ضع الـ SVG داخل `.hero-bg` مع `width="100%" height="100%"`.
- **#1:** داخل `.flow` مع `width="100%"`.
- تأكد أن كل SVG فيه `viewBox` وبدون `width/height` ثابتة (أو احذفها) ليتجاوب.
- أيقونات زخرفية: أبقِ `aria-hidden="true"`.

### 3. تعديلات يدوية بعد التجميع
- [ ] استبدل الألوان في `:root` بالأكواد الرسمية لسينكرو.
- [ ] ضع رابط الفيديو (iframe) واحذف `.video-ph`.
- [ ] اربط الفورم: `action` لفورم GHL/Webhook، أو انقل الحقول لـ Form Builder في GHL وانسخ نفس الـ CSS.
- [ ] فعّل أكواد التتبع (Pixel/GA4) وحرّر التعليق في الـ `submit`.
- [ ] أكمل قائمة الدول أو استخدم `intl-tel-input` + تحديد الدولة تلقائياً.
- [ ] روابط الشروط والخصوصية.
- [ ] اختبر على جوال حقيقي: الزر الأول ظاهر بدون سكرول؟
- [ ] احذف البند الخامس من الفوائد إذا ربط الإعلانات غير مفعّل في التجربة.
- [ ] اعتماد Muhammad.

### في GoHighLevel
- أنشئ صفحة → **Custom Code / HTML element** والصق الملف كاملاً، أو قسّمه: الـ `<style>` في Custom CSS، والأقسام كـ HTML blocks، والبوب أب = GHL Popup بفورم GHL (أنظف للأتمتة).
