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

---

# 4. الدفعة الثانية — ما قُرئ وما نطبّقه

## ⭐ اكتشاف مهم: «GoOnline Smart Growth Platform» (عرض الوكالة نفسها للمطاعم — فبراير 2026)
منصة GHL للمطاعم: WhatsApp + أتمتة + CRM + ولاء + تقييمات + حجوزات + صفحات هبوط + AI chatbot.
| العنصر | التفاصيل |
|---|---|
| 6 آلات | Lead Capture • Loyalty Engine (4 مستويات: الاحتياطي/الأساسي/الكابتن/الأسطورة) • Reactivation (30 يوم) • Review Machine (4–5 نجوم ← Google، 1–3 ← المالك) • Seasonal Campaigns (رمضان، الكلاسيكو، العيد، الثلاثاء) • B2B/Franchise Pipeline |
| الباقات | Starter $150 • Operator $300 (الأكثر شيوعاً) • Champion $500 — شهري، إلغاء بأي وقت، إعداد وإدارة كاملة |
| خطة 90 يوم | يوم بيوم (إعداد ← حملات ← توسيع) |
| مؤشرات | 1,000 عميل بالـ CRM شهر 1، 5,000 شهر 3؛ 200+ تقييم؛ 10%+ استرجاع |

> ❓ **قرار مطلوب:** وصفك الأول للخدمة («GHL + أدوات ميتا وقوقل + ربط المطعم لمعرفة مصدر الشراء») يطابق **Smart Growth** أكثر من سينكرو. سينكرو = نظام طلبات/كاشير (SaaS $39)، وSmart Growth = خدمة تسويق وأتمتة مُدارة ($150–500). **هم منتجين يكمّلوا بعض** (سينكرو يجيب الطلب، Smart Growth يرجّع الزبون). الملفات `01–13` مبنية على سينكرو. نحتاج نعرف: هل المشروع لسينكرو فقط، أو Smart Growth، أو باقة مشتركة؟

## مطاعم سابقة (خبرة الوكالة — أمثلة واقعية للأفاتار والمحتوى)
| الملف | ما نأخذه |
|---|---|
| **Content Strategy – مدغدغ** | 5 أعمدة محتوى (الطريقة 30%، الأكل 25%، حب الزبائن 20%، المجتمع 15%، العروض 10%) • فيسبوك أساسي بالأردن • خطة رمضان أسبوعية + أوقات النشر الرمضانية • ميزانية مرجعية 400–500 دينار/شهر • قياس «من وين عرفتنا؟» |
| **Proposal – مدغدغ** | أفكار ابتكارية (First Bite Challenge، Secret Menu Club، QR على كل صينية، ASMR بدون موسيقى) • إعلانات بنطاق 5 كم + Google Maps |
| **Chickano – خطة 6 شهور** | تسلسل: تصوير منيو ← هوية ← سفير براند ← مؤثرين ← رمضان/عيد ← صيف |
| **WC2026 Campaign Playbook** | حملة ولاء كاملة على GHL + Boomerangme: 10 أتمتة، Tags/Custom Fields، 10 رسائل واتساب بالأردني، منيو موسمي — **قالب ممتاز لحملة «Seasonal» في سينكرو/Smart Growth** |
| **Abu Alkhair Knowledge Base** | نموذج Knowledge Base لبوت واتساب مطعم (ساعات، دفع، توصيل، FAQ، منيو) — **قالب جاهز لبونص «بوت الرد» أو لـ onboarding العملاء** (يحوي بيانات تواصل عميل — لا يُنسخ للريبو) |

**➜ تحديث الأفاتار:** السوق الأردني: فيسبوك هو المنصة الأولى للعائلات، والأولوية لرمضان/العيد/المباريات كمواسم شراء. الألم المتكرر في ملفات الوكالة: «ما نعرف المبيعات جاية من وين» + الاعتماد على Talabat.

## الأتمتة والتتبع
| الملف | ما نطبّقه على سينكرو |
|---|---|
| **SOP-GHL-Calendar-Meta-Pixel** | الـ Widget داخل iframe → الـ Pixel على الصفحة ما بيشوفه. **قاعدة:** اختار مسار واحد (Pixel أو CAPI أو أسماء أحداث مختلفة) لتجنّب العدّ المزدوج • Custom Conversion بالـ URL • جلسة الخبير $40 لو بتقويم GHL تحتاج Pixel ID بالتقويم |
| **HighLevel Attribution Guide** | سكريبت يحفظ UTM/fbclid/gclid في sessionStorage ويعبّي حقول مخفية بالفورم (`data-q`) → **يُضاف لـ `pages/optin.html` و`sales.html`** + Custom Fields بالـ CRM |
| **8_CRM_Automation_Build_Guide** | نمط بناء: Pipeline مراحل واضحة • **Global filter** (`do-not-contact`) على كل Workflow • Internal Notification + Task للمسؤول • Reply Capture (رد ← Tag) • عدّادات (Math) • قوالب واتساب تُعتمد مسبقاً |
| **RESALA Automation** | ⭐ **تقسيم حسب مشاهدة الفيديو:** شاهد <25% ← رسائل «كمّل الفيديو» (1س/12س/24س/48س)؛ شاهد >25% ← دعوة للخطوة التالية. + Abandoned Form بعد ساعة. → **يطبّق على صفحة الـ VSL:** من فتح البوب أب ولم يسجّل، ومن شاهد الفيديو ولم يضغط |
| **Automation Checklist** | (مطبّق في القسم 1) |

## الإيميلات والواتساب (أطر)
| الملف | النمط |
|---|---|
| **Abandoned Cart (4 إيميلات)** | 1) «مشكلة تقنية؟» 2) «حجزنا مكانك 24 ساعة» 3) «كفّة الميزان» 4) «منتصف الليل» — نستخدم 1 و3 فقط (بدون ندرة مزيفة) |
| **Post-Purchase (5)** | وصول ← «طبّقت؟» + تحدي صغير ← دعوة لجلسة ← «ليش يفشلوا» ← «نغلق الملف؟» |
| **منهجية رسالة – فانل كامل** | 5 هيرو بديلة • إيميلات Abandoned/Confirmation/Follow-up • واتساب بأزرار تفاعلية • **جدول تصاميم: COPY × STYLE × HOOK ANGLE × AWARENESS** • 15 سكريبت ريلز (حوار مبتدئ/خبير، وايت بورد، مقارنة) |
| **SOP Adscope** | (مطبّق في `12` و`13`) |

**➜ ما نضيفه لسلسلة `07`:** (أ) رسائل واتساب بأزرار تفاعلية: «ربطت الجهاز ✅ / محتاج مساعدة» (ب) مسار «فتح البوب أب ولم يسجّل» بعد ساعة (ج) مسار مشاهدة الفيديو <25%.
**➜ ما نضيفه للإعلانات `13`:** جدول تصاميم بنمط COPY/STYLE/HOOK/AWARENESS + سكريبتات ريلز حوار (صاحب مطعم/خبير).

## أدوات وموارد
- **Ai Agents:** قائمة GPTs/Gems لإسلام صلاح (Hakeem تشخيص، Huwia عرض، Rabeh LTO، Sultan صفحات، Bassel VSL، Murad إيميل، Omar واتساب، Zaki فيديو، Rami هوكات) — روابط خارجية لا تُشغّل من هنا.
- **GHL Funnel Template Bundle:** 50+ قالب GHL جاهز (منها **Saas Funnel**، **Webinar/VSL Optin**، **Automated VSL**، **Upsell Sales Page**) — مناسب كبداية للبناء الفعلي.
- **Funnel Design Form (Kayan):** استمارة جمع بيانات العميل قبل التصميم → **نعتمدها كجزء من SOP النسخ لقطاعات أخرى.**
- **قائمة بونصات عرض الـ1000:** (النص مقلوب بالـ PDF) أنواع: Swipe files، Templates، SOPs، Fast-action، Done-with-you، ضمان، جلسة 1:1، Checklists، بونص سري بعد الشراء.

## لم يُقرأ بعد (كبير/مكرر/خارج النطاق)
Resala High Ticket Funnel V2 • تحدي القمة AI (+نسخة) • تحدي السيستم الذكي • تحدي مضاعفة القيمة • C.Boran masterclass • Email Sequences بوصلة البزنس • Coach Manar/Balqis • Wilys (pptx + محتوى) • VOYO • صفحات هبوط مميزة • ملفات مشاريع Adscope (Tanaghum/Dalya/Ghizlan…) — معظمها لمدربين/كورسات؛ نقرأها عند الحاجة لنمط معيّن.
