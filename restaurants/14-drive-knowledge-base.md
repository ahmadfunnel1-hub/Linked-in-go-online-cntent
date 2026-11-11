# 14 — مرجع المعرفة من Google Drive (gonlineagency)

> المصدر: درايف gonlineagency@gmail.com (ملفات مملوكة + «تمت مشاركتها معي»). الحسابات الأخرى (ahmadfunnel1، ahmadotaibidmy123) غير مربوطة مباشرة؛ ما يُشارك منها مع gonlineagency يظهر هنا.
> ⚠️ كثير من الملفات تخص عملاء آخرين. نأخذ منها **الأطر والهياكل** فقط — لا ننسخ نصوصهم ولا بياناتهم.

## 1. ما تمت قراءته وتطبيقه

### أ) SOP — تحسين Meta Pixel + Conversions API في GHL (ahmadfunnel1)
**يُطبّق على سينكرو في مرحلة الأتمتة/التتبع:**
- قبل أي إضافة: حدد **مصدر الـ Server Events** (GHL؟ Partner؟ Custom؟). ممنوع إضافة Pixel/CAPI جديد قبلها.
- **Automatic Events = OFF**؛ CAPI Settings: connect only your datasets = ON، shared = OFF.
- **نفس `event_id` للمتصفح والسيرفر لنفس الحدث** (Deduplication) — أولوية 1.
- **fbc** لا يُرسل فارغاً من السيرفر (fbclid → _fbc → CAPI) — أولوية 2. **fbp** يُلتقط مبكراً ويمرَّر — أولوية 3.
- إرسال Email/Phone/External ID للأحداث المهمة بعد صحة البنية — أولوية 4. Parameter Builder اختياري.
- اختبار برحلة حقيقية في **Test Events** (Ad → Landing → PageView → Form → الحدث) والتحقق من: Event ID، fbp، fbc، URL، IP، UA.
- معايير الإغلاق: Coverage ≥ 75%، Dedup best-practice، لا أحداث مكررة.
**➜ تعديل خطة سينكرو:** حدث `StartTrial` (بدل Lead) و`Subscribe` يتبعان نفس القواعد؛ نرسل الهاتف (مع كود الدولة) كـ match key.

### ب) Automation Checklist (فريق الأتمتة)
إطار جاهز لـ GHL (Low-ticket / Webinar). **ما ينطبق على سينكرو بعد تكييفه للتجربة المجانية:**
| من الـ Checklist | المقابل في سينكرو |
|---|---|
| Abandoned Cart (فورم opt-in بدون شراء → 30د → شرط Tag → إيميل+واتساب ×3) | **«بدأ التسجيل ولم يُكمل»** (فتح البوب أب/صفحة بدون إرسال) — يحتاج حدث جزئي، وإلا يُستبدل بريتارجت ميتا |
| Purchase Sequence (Payment received → Tag → إزالة من السلاسل → Conversion tracking → رسالة واتساب تفاعلية بفرعين) | **Trial started** → Tag `trial_started` → سلسلة التفعيل (`07`). وعند **Subscribe** → Tag `customer` + إزالة من سلسلة التجربة + تتبع التحويل + واتساب تفاعلي: «ربطت الجهاز؟ نعم/لا» → «لا» = إشعار داخلي للدعم |
| Upsell/Downsell sequences | إضافات (ولاء/فروع/تاسكس/آدز) و«313 تدير إعلاناتك»؛ Downsell = جلسة خبير $40 |
| Reply sequence (كلمة مفتاحية على واتساب → رابط) | ردّ «مساعدة» → رابط فيديو ربط Sunmi؛ «سعر» → صفحة الباقات |
| Sales Pipeline | مراحل: Trial started → Device connected → First order → Day 12 → Subscribed / Lost → Downsell |
| Conversion Tracking workflow | يُبنى حسب SOP الـ CAPI أعلاه |
| Call sequences | ❌ لا ينطبق (ملف الهوية يمنع الاستشارات المجانية) — فقط تأكيد/تذكير جلسة الخبير المدفوعة |

### ج) Tamayoz Automation (عميل آخر)
سلسلة إيميلات تسويقية لمعسكر — **مرجع أسلوب فقط** (افتتاح بسؤال عاطفي، تحدي صغير داخل الإيميل، توقيت كل 5 أيام). لا ينطبق محتوى.

## 2. فهرس المصادر المكتشفة (للقراءة حسب المرحلة)
| المرحلة | الملفات |
|---|---|
| **التتبع والأتمتة** | SOP-GHL-Calendar-Meta-Pixel • HighLevel Attribution Reporting Guide • 8_CRM_Automation_Build_Guide_EN • RESALA Automation • GHL_Power_Plan_Legend_x_Wilys |
| **هياكل الفانل** | The Ultimate GHL Funnel Template Bundle • Funnel Design Template (Kayan.ai) • Resala High Ticket Funnel V2 • تحدي القمة AI (فانل كاملة) • منهجية رسالة 2026 • خطة تنفيذ منهجية الرسالة • صفحات هبوط مميزة |
| **الإيميلات والواتساب** | Email Sequences بوصلة البزنس • إيملات ما بعد الشراء • Abandoned Cart Sequence • Call Confirmation emails • C.Boran Ad scripts + Emails + WA |
| **الإعلانات** | إعلانات معسكر التميّز • (SOP Adscope — مطبق في `12`) |
| **العروض والبونصات** | قائمة بونصات قوية لعرض الـ 1000 • GoOnline_SmartGrowth_Platform |
| **المطاعم (خبرة سابقة)** | مجلد Restaurants • Content Strategy مطعم مدغدغ + Proposal • Chickano Marketing Strategy • Wilys • منيوهات شاوبرز وأبو مويس |
| **قوائم عملاء محتملين (عمّان)** | luxury_amman_venues (100 + emails) • all_500_raw_results — ⚠️ بيانات شخصية: استخدامها للتواصل يحتاج أساس قانوني/موافقة |
| **أدوات Gemini (Gems)** | Sultan (Funnel copy) • Murad (Email) • Omar (WA) • Khaldun (Ads) • Script DNA — لا يمكن تشغيلها من هنا، فقط وصفها |

## 3. الخطوة التالية
قراءة مجموعة «التتبع والأتمتة» كاملة قبل بناء GHL، ثم «المطاعم» لتحديث الأفاتار والعروض بأمثلة واقعية.
