# صفحة معتز مشعل — خطة الـ 90 يوم | تطبيق على GHL

تنفيذ التصميم المرفق كـ **Custom HTML** جاهز للصق داخل فَنِل GHL.
عربي RTL، موبايل أول، والنموذج بيضل **عنصر GHL أصلي** — يعني الليدز بتنزل
عالـ CRM والـ Workflows بتشتغل عادي بدون أي middleware.

مرجع التصميم: [`assets/design-reference.jpg`](assets/design-reference.jpg)

---

## الملفات

| الملف | وين بينحط في GHL |
|---|---|
| `01-head-tracking.html` | Funnel → Settings → Tracking Code → **HEAD** |
| `02-page-custom-css.css` | Page Builder → Settings (الترس) → **Custom CSS** |
| `03-hero-custom-html.html` | Section 1 → Add Element → **Custom JS/HTML** |
| `04-booking-custom-html.html` | Section 2 → Add Element → **Custom JS/HTML** |
| `assets/hero-placeholder.svg` | للمعاينة المحلية بس — مش للرفع |
| `build-preview.sh` | بيبني `preview.html` من نفس الملفات فوق |
| `preview.html` | مولّد — لا تعدّل عليه، عدّل على الأصل وأعد البناء |

---

## خطوات التركيب (٦ خطوات)

### 1) الهيد
افتح الفَنِل → **Settings → Tracking Code → HEAD** → الصق `01-head-tracking.html` كامل → Save.
هاد بيجيب الخطوط العربية (Tajawal + Aref Ruqaa) وبيظبط `dir="rtl"` على مستوى الصفحة.

### 2) ارفع صورة معتز
**Media Library → Upload** → انسخ الرابط.

مواصفات التصدير:
- **PNG خلفية شفافة** (قصّة للشخص لحاله) — هاي الأفضل، بتندمج مع خلفية الصفحة الكريمية.
- العرض: **1200px** كحد أدنى، الارتفاع حسب القصة.
- الحجم: تحت **250KB** (اضغطها بـ TinyPNG).
- بديل: صورة مستطيلة عادية بخلفية القاعة — بتشتغل كمان، بس بدّل بملف `03`:
  `object-fit: contain` → `object-fit: cover`

### 3) بلوك الهيرو
سكشن جديد → **Add Element → Custom JS/HTML** → الصق `03-hero-custom-html.html` كامل.

بعدها بدّل سطر واحد بس:
```html
<img class="mmlp-photo-img" src="HERO_IMAGE_URL" ...>
```
حط مكان `HERO_IMAGE_URL` رابط الصورة من الخطوة 2.

> إذا نسيت تبدّلها، بتطلع خانة منقّطة مكتوب عليها "ضع صورة معتز هنا" بدل
> أيقونة صورة مكسورة — يعني ما بتنكشف قدام العميل.

### 4) ستايل السكشن
اضغط على **الـ Section** اللي حطيت فيه الهيرو → **Advanced → Custom CSS Class** →
اكتب `mmlp-section`.
بعدها: Page Settings → **Custom CSS** → الصق `02-page-custom-css.css`.

هاد بيلغي الـ padding اللي GHL بيحطه حوالين الـ Custom HTML، وبدونه بتطلع
هوامش بيضا بتكسر الـ full-bleed تبع الصورة.

### 5) سكشن الحجز + النموذج
سكشن تاني تحت الهيرو → **Add Element → Custom JS/HTML** → الصق `04-booking-custom-html.html`.

بعدها **بنفس الـ Row**، حط عنصر GHL الأصلي:
**Add Element → Form** (أو Survey أو Calendar) → اختار الفورم →
**Advanced → Custom CSS Class** → اكتب `mmlp-formhost`.

بينلبس تلقائياً ستايل الكرت الأبيض تبع بقية الصفحة.

> ⚠️ لا تحط الفورم كـ HTML جوّا البلوك. عنصر GHL الأصلي هو اللي بيوصل الليد
> للـ CRM وبيشغّل الـ Workflows. البلوك بس غلاف.

### 6) الزر
زر "احجز مقعدك الآن" بيسكرول لـ `#booking` تلقائياً — ما بده أي إعداد.
إذا بدك يروح لصفحة تانية (مثلاً checkout مباشرة)، بدّل بملف `03`:
```html
<a class="mmlp-cta" href="#booking" data-mmlp-cta>
```
→
```html
<a class="mmlp-cta" href="/checkout">
```
(شيل `data-mmlp-cta` حتى يوقف السكرول ويصير لينك عادي)

---

## تمرير الـ UTM للـ Workflows

سكربت البلوك بياخذ الـ UTM من رابط الصفحة وبيحقنها جوّا iframe الفورم
تلقائياً — `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`,
`utm_content`, `gclid`, `fbclid`, `ttclid`, `ref`.
وبيخزّنها بالـ `sessionStorage` كمان، فلو الزائر تنقّل بين صفحات الفَنِل
بتضل محفوظة لحد ما يعبّي.

**ليش مهم:** لما تشغّل أكثر من حملة على نفس الصفحة، عزل الـ Workflows
بالتاغات بيعمل race condition — التاغين بينحطوا بنفس اللحظة.
العزل الصحيح بالـ UTM:

```
Workflow A → Trigger: Form Submitted + utm_campaign = moataz_oct_meta
Workflow B → Trigger: Form Submitted + utm_campaign = moataz_oct_google
```

GHL بينشئ الـ custom fields لحاله من مفاتيح الـ payload — ما بدك تعملهم يدوي.

روابط الحملات:
```
https://YOUR-DOMAIN/moataz-90?utm_source=meta&utm_campaign=moataz_oct_meta
https://YOUR-DOMAIN/moataz-90?utm_source=google&utm_campaign=moataz_oct_google
```

---

## المعاينة قبل النشر

```bash
bash ghl/build-preview.sh
```
بيولّد `ghl/preview.html` من نفس ملفات GHL — افتحه بالمتصفح، وجرّبه على
عرض 390px (موبايل) و 1280px (ديسكتوب).

**مصدر واحد للحقيقة:** `preview.html` مولّد. أي تعديل بيصير على الملفات
`01`–`04`، وبعدها تعيد البناء. لا تعدّل على `preview.html` مباشرة.

---

## تعديلات سريعة

**الألوان** — أول 12 سطر بالـ `<style>` تبع ملف `03`:
```css
--mm-gold:    #B8873B;   /* الذهبي الأساسي */
--mm-gold-lt: #C9A35C;   /* فاتح — نهاية الـ gradient */
--mm-gold-dk: #96682A;   /* غامق — بداية الـ gradient */
--mm-ink:     #1C1917;   /* لون العناوين */
--mm-cream:   #FCF9F4;   /* خلفية الصفحة */
```

**النصوص والتواريخ** — كلها HTML عادي بملف `03`، عدّل مباشرة.
المكان والتاريخ والمدة بالـ `<ul class="mmlp-facts">`.

**الأرقام** — `<ul class="mmlp-stats">`.

**الزر الثابت تحت** (مش موجود بالتصميم الأصلي — مضاف لأنه بيرفع التحويل
على الموبايل): بيطلع لما يختفي زر الهيرو، وبيختفي لما يوصل الزائر لسكشن
الحجز. إذا ما بدك إياه، امسح من ملف `03`:
```html
<div class="mmlp-sticky" data-mmlp-sticky hidden> ... </div>
```

---

## ملاحظات GHL

- **ممنوع `all: revert`** جوّا أي custom CSS هون — بيكسّر ستايلات GHL الأصلية،
  وبالذات لو استعملت popups لاحقاً.
- كل الستايل مُقيّد تحت `.mmlp` — ما بيأثر على أي عنصر تاني بالصفحة ولا على الـ builder.
- الريسِت مكتوب بـ `:where()` عشان specificity = صفر، فقواعد المكوّنات بتغلبه.
  إذا ضفت قواعد جديدة، خليها بنفس النمط.
- لو حطيت **popup** بدل السكرول، استعمل نمط الـ interval المعروف على
  الزر الأصلي (`.click()` على الحاوية ما بتشتغل).
- الـ `<script>` بالبلوك بيشتغل مرة وحدة وبيوقف مراقبة الـ DOM بعد 8 ثواني —
  ما بيأثر على أداء الصفحة.
