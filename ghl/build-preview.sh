#!/usr/bin/env bash
# يبني ملف preview.html من نفس ملفات GHL — مصدر واحد للحقيقة.
# التشغيل:  bash ghl/build-preview.sh   ثم افتح ghl/preview.html بالمتصفح.
set -euo pipefail
cd "$(dirname "$0")"

{
  printf '<!doctype html>\n<html lang="ar" dir="rtl">\n<head>\n<meta charset="utf-8">\n'
  printf '<title>معتز مشعل — خطة الـ 90 يوم</title>\n'
  # الهيد: نفس ملف GHL بدون سطور التعليق
  perl -0pe 's/<!--.*?-->//gs' 01-head-tracking.html
  printf '<style>\n'
  cat 02-page-custom-css.css
  printf '\nbody{margin:0}\n</style>\n</head>\n<body>\n'
  # البلوكات: نفس الملفات، مع تبديل رابط الصورة بالـ placeholder المحلي
  sed 's|src="HERO_IMAGE_URL"|src="assets/hero-placeholder.svg"|' 03-hero-custom-html.html
  cat 04-booking-custom-html.html
  # مكان نموذج GHL الأصلي — تمثيل بصري فقط بالمعاينة
  printf '<div class="mmlp" dir="rtl"><div class="mmlp-wrap mmlp-wrap--narrow" style="padding-bottom:96px">'
  printf '<div class="mmlp-formhost" style="display:grid;place-items:center;min-height:300px;color:#A8A29E;font-family:Tajawal,sans-serif;font-size:14px;text-align:center;line-height:2">'
  printf 'هون بينحط عنصر GHL الأصلي<br>(Form / Survey / Calendar)<br>مع Custom CSS Class = mmlp-formhost'
  printf '</div></div></div>\n'
  printf '</body>\n</html>\n'
} > preview.html

echo "✅ ghl/preview.html جاهز"
