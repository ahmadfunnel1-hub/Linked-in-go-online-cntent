# «أثرٌ يبقى» — فنل تسجيل لقاء مجاني مع الشيخ علاء جابر (GoHighLevel)

## السياق
- المالك: أحمد (Go Online). خبير GHL. الردود بالعربي الشامي، مختصرة ومباشرة.
- لا تخترع أرقام أو شهادات أو نتائج. أي معلومة ناقصة تضل placeholder `[...]`.
- الدومين: alaa-jaber.com
- صفحة التسجيل: `https://alaa-jaber.com/mecca-madinah-webinar` (اسم الـ slug قديم، الصفحة هي «أثرٌ يبقى»)
- صفحة الشكر: `https://alaa-jaber.com/mecca-madinah-webinar-thankyou`

## الملفات
| الملف | وين بينلصق |
|---|---|
| `athar-yabqa/register-part-a.html` | Custom Code #1 بصفحة التسجيل (الهيرو لحد سكشن «احجز مقعدك») |
| `athar-yabqa/register-part-b.html` | Custom Code #2 (الأسئلة، الختام، الفوتر، الشريط الثابت) |
| `athar-yabqa/register-popup-c.html` | Custom Code #3 بآخر الصفحة: البوب أب |
| `athar-yabqa/thank-you.html` | Custom Code واحد بصفحة الشكر |
| `athar-yabqa/emails/*.html` | قوالب LC Email (تأكيد + 24h + 3h + 15m) |
| `*-preview.html` | معاينة بالمتصفح فقط. **لا تنلصق بـ GHL** |
| `reference-lara/lara-hero-and-popup-WORKING.html` | كود صفحة ورشة لارا: البوب أب **شغّال هناك** ويرسل لفورم GHL |

- إعدادات الموعد والواتساب بأول سكريبت Part A: `EVENT_START` و `EVENT_DATE_TX` و `EVENT_TIME_TX` و `VIDEO_ID` و `WHATSAPP_NUMBER`. لسا placeholders.
- Part A بيعرّف `window.AY_EVENT` اللي بيقرأه البوب أب.
- Prefixes: `.ay` للتسجيل، `.ayt` للشكر، `.ayp` للبوب أب.

## 🔴 المشكلة المفتوحة: التسجيل ما بيوصل GHL
**الهدف:** أي زر `href="#register"` يفتح بوب أب بتصميم «أثرٌ يبقى» (زيتي وذهبي). البيانات توصل لفورم GHL الأصلي، فيتعمل Contact ويشتغل Workflow (Form Submitted)، وبعدها يتحوّل لصفحة الشكر.

**الوضع الحالي:**
- Part C (v4) هو **نسخة حرفية من منطق بوب أب لارا**: يعبّي الحقول المخفية ويضغط زرها عن بُعد. `GHL_SECTION_ID = 'section-WN5i3fo8Fm'` و `HIDE_GHL_FORM = true`.
- النتيجة: البوب أب بيطلع «تم حجز مقعدك»، **بس ما في Contact ولا Workflow اشتغل**.
- ⚠️ رسالة النجاح بتطلع **دايمًا** بعد 1.5 ثانية، حتى لو الإرسال فشل، لأنها هيك بكود لارا الأصلي. لازم تنربط بتأكيد حقيقي.

**شو انجرّب وفشل:**
1. **v1/v2:** نفس فكرة الـ bridge. الـ Console أكد إنه لقى `full_name` و `email` و `phone` والزر «سجل حضورك الان مجانا» وعبّاهم، بس **ولا طلب submit طلع** (عملنا hook على fetch/XHR بالـ regex `(forms?|surveys?)/submit`).
2. **v3:** نقل الـ Form element الحقيقي لجوّا البوب أب. أحمد عبّاه **بإيده** وضغط، وبرضو **ما انعمل Contact**. الشكل كمان خرب (أيقونة الإيميل كبرت).

**الاستنتاج المرجّح:** فورم GHL نفسه على هالصفحة **ما بيرسل حتى يدويًا**. يعني المشكلة غالبًا مش بالبوب أب.

**أول خطوة لازم تنعمل** (ما انعملت لسا):
1. شيل Part C من الصفحة، وعبّي فورم GHL الأصلي بإيدك على الصفحة المنشورة، وشوف إذا بينعمل Contact.
2. افتح DevTools ← Network وشوف شو بيصير لما تضغط الزر: هل في طلب؟ هل في خطأ validation أو captcha؟ هل الزر بيرجع للـ funnel؟
3. اتأكد من إعدادات الفورم:
   - Captcha
   - الحقول الإجبارية
   - On Submit (Redirect)
   - هل هو نفس فورم لارا؟ نص الزر «سجل حضورك الان مجانا» من فورم لارا
   - هل الفورم تابع لنفس الـ Location تبع الفنل؟
4. احتمال إنه Part A أو Part B فيهم شي بيتعارض مع فورم GHL: CSS بـ `!important` على `.ay-form`، أو سكريبت بيلقط الكليك. جرّب الفورم يدوي مع وبدون Part A/B.
5. بعد ما الفورم اليدوي يشتغل:
   - رجّع Part C (bridge).
   - اربط رسالة النجاح بتأكيد حقيقي (اختفاء الفورم، أو رد الـ submit request).
   - تحويل لصفحة الشكر.

**البديل المضمون إذا ضل الـ bridge مش شغال:** Embed الفورم كـ iframe (Forms ← Integrate) جوّا البوب أب، وتنسيقه من Form Builder.

## الـ Workflows (الطريقة B، معتمدة)
1. **Form Submitted** (فورم أثرٌ يبقى) ← Tag `athar-registered` ← Update Contact Field `athar_event_date` (Date+Time) ← إيميل التأكيد + WhatsApp Template ← If/Else: لو Date Added بعد (الموعد ناقص 15 دقيقة) يبعث رابط الدخول فورًا.
2. Workflows 2 و3 و4: Trigger `Custom Date Reminder` على `athar_event_date`، Before 24h / 3h / 15m، فلتر Tag `athar-registered`، ثم إيميل + واتساب.
   - المسجّل المتأخر بيتخطى التذكيرات اللي فات وقتها تلقائيًا.
   - تأكد إنه التريجر بيقبل ساعات ودقائق. البديل: Email Campaign مجدول.
- Custom Values المطلوبة: `athar_date` و `athar_time` و `athar_link`.
- ⚠️ لازم **فورم جديد خاص بأثرٌ يبقى**، مش فورم لارا، وإلا التسجيلات بتشغّل Workflow لارا.
