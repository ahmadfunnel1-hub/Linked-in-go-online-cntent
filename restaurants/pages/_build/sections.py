"""Builds the 25 sections (fixed order) from one content dict. Section numbers match the brief."""
from engine import R, cta, band, countdown

def _li(items):
    return ''.join('<li>' + i + '</li>' for i in items)

def build(d):
    s = []
    # 1 HERO (dark photo background)
    when = ''.join('<span>' + a + ' <b>' + b + '</b></span>' for a, b in d['when'])
    s.append('<section class="hero"><div class="in">'
             '<span class="season">' + d['season'] + '</span>'
             '<h1>' + d['h1'] + '</h1><p class="lead">' + d['hero_lead'] + '</p>'
             '<div class="when">' + when + '</div>' + countdown() + cta(d['cta_sub']) + '</div></section>')
    # 2 PROVOCATIVE REFRAME
    s.append(band('light', '<div class="c reframe rv"><span class="eye">' + d['reframe_eye'] + '</span><h2>' + d['reframe_h2'] + '</h2>'
                  '<p class="lead mut narrow">' + d['reframe_sub'] + '</p></div>'))
    # 3 LET ME GUESS HOW YOUR WEEK GOES
    days = ''.join('<div class="dy"><b>' + a + '</b><span>' + b + '</span></div>' for a, b in d['week_days'])
    s.append(band('soft', '<div class="week"><div class="rv"><span class="eye">' + d['week_eye'] + '</span><h2>' + d['week_h2'] + '</h2>'
                  '<div class="days">' + days + '</div></div>'
                  '<div class="story rv"><span class="eye" style="background:rgba(255,255,255,.12)">' + d['story_eye'] + '</span>'
                  '<p>' + d['story_body'] + '</p><div class="big">' + d['story_num'] + '</div><p class="mut">' + d['story_num_label'] + '</p></div></div>'
                  '<p class="insight rv">' + d['insight'] + '</p>'))
    # 4 NAME THE SOLUTION AS A ROLE
    s.append(band('brand', '<div class="c role narrow rv"><h2>' + d['role_h2'] + '</h2><p class="lead mut">' + d['role_p'] + '</p>' + cta() + '</div>'))
    # 5 DAY-IN-THE-LIFE GRID
    cards = ''
    for i, (ic, t, b) in enumerate(d['grid']):
        cards += ('<div class="card rv' + (' fun' if i == 5 else '') + '"><span class="ic">' + ic + '</span>'
                  '<h3>' + t + '</h3><p>' + b + '</p></div>')
    s.append(band('dark', '<div class="c rv"><span class="eye" style="background:rgba(255,255,255,.12)">' + d['grid_eye'] + '</span><h2>' + d['grid_h2'] + '</h2></div>'
                  '<div class="grid6">' + cards + '</div><p class="sub6 c">' + d['grid_sub'] + '</p>'))
    # 6 TRUST LINE
    s.append(band('brand', '<div class="c narrow rv"><h2>' + d['trust_h2'] + '</h2><p class="lead mut">' + d['trust_p'] + '</p></div>'
                  '<div class="vs rv"><div class="side"><h3>' + d['vs_tool'][0] + '</h3><ul>' + _li(d['vs_tool'][1]) + '</ul></div>'
                  '<div class="x">مقابل</div><div class="side us"><h3>' + d['vs_sys'][0] + '</h3><ul>' + _li(d['vs_sys'][1]) + '</ul></div></div>' + cta()))
    # 7 DIFFERENTIATION BAND
    meta = ''.join('<div><b>' + a + '</b><p class="mut">' + b + '</p></div>' for a, b in d['diff_meta'])
    s.append(band('dark', '<div class="narrow c rv"><h2>' + d['diff_h2'] + '</h2><p class="lead mut">' + d['diff_p'] + '</p></div>'
                  '<div class="meta rv">' + meta + '</div><div class="c"><div class="stat rv">' + d['diff_stat'][0] + '<span class="mut">' + d['diff_stat'][1] + '</span></div></div>' + cta()))
    # 8 INTRODUCING
    s.append(band('brand', '<div class="c intro narrow rv"><span class="eye" style="background:rgba(255,255,255,.16)">أقدّملك</span>'
                  '<div class="name">' + d['name'] + '</div><p class="lead">' + d['intro_p'] + '</p><p class="tagline">' + d['tagline'] + '</p></div>'))
    # 9 STACK ITEM 01 — the live event
    dd = ''.join('<div><span class="k">' + k + '</span><b>' + b + '</b><p>' + t + '</p></div>' for k, b, t in d['days'])
    i1 = ('<div class="item rv"><span class="no">01</span><div><h3>' + d['ev_title'] + '</h3>'
          '<div class="meta-row">' + ''.join('<span>' + a + ' <b>' + b + '</b></span>' for a, b in d['ev_meta']) + '</div>'
          '<div class="dd">' + dd + '</div>'
          + ('<p style="margin-top:14px">' + d['ev_extra'] + '</p>' if d.get('ev_extra') else '') +
          '<p class="val">القيمة: ' + d['ev_value'] + '</p>'
          '<div class="ph" style="margin-top:16px">' + R('فيديو قصير أو رأي حقيقي عن الورشة (بموافقة مكتوبة)') + '</div></div></div>')
    s.append(band('brand', '<div class="c rv"><h2>' + d['stack_h2'] + '</h2></div>' + i1, id_='xo-stack'))
    # 10 STACK ITEM 02 — system / templates
    mini = ''.join('<div><b>' + a + '</b>' + b + '</div>' for a, b in d['it2_mini'])
    s.append(band('brand', '<div class="item rv" style="margin-top:0"><span class="no">02</span><div><h3>' + d['it2_title'] + '</h3>'
                  '<p style="margin-top:8px">' + d['it2_p'] + '</p><div class="mini">' + mini + '</div>'
                  '<p class="val">القيمة: ' + d['it2_value'] + '</p></div></div>'))
    # 11 STACK ITEM 03 — recurring product + No-Surprises Promise
    if d.get('it3_title'):
        s.append(band('brand', '<div class="item rv" style="margin-top:0"><span class="no">03</span><div><h3>' + d['it3_title'] + '</h3>'
                      '<p style="margin-top:8px">' + d['it3_p'] + '</p>'
                      '<div class="promise"><b>وعد «بدون مفاجآت»</b><ul>' + _li(d['it3_promise']) + '</ul></div>'
                      '<p class="val">القيمة: ' + d['it3_value'] + '</p></div></div>'))
    else:
        s.append('')
    # 12 BONUS MARQUEE
    words = ('<span>بونص</span><span>•</span>' * 14)
    s.append('<div class="mq" aria-hidden="true"><div class="tr">' + words + words + '</div></div>')
    # 13 THREE BONUSES
    bn = ''
    for i, (name, kills, txt, val) in enumerate(d['bonuses']):
        bn += ('<div class="bn rv"><span class="n mono">BONUS 0' + str(i + 1) + '</span><h3>' + name + '</h3>'
               '<p class="kills">بيقتل عذر: <s>«' + kills + '»</s></p><p>' + txt + '</p><p class="val">القيمة: ' + val + '</p></div>')
    s.append(band('brand', '<div class="c narrow rv"><h2>' + d['bonus_h2'] + '</h2><p class="lead mut">' + d['bonus_p'] + '</p></div>'
                  '<div class="bonus">' + bn + '</div>' + cta()))
    # 14 BORROWED AUTHORITY (only if real)
    s.append(band('light', '<div class="narrow c rv"><span class="eye">شهادة من برّا</span><div class="ph">' + R('شهادة طرف ثالث حقيقية (فيديو أو اقتباس) بموافقة مكتوبة. إذا ما في، احذف هالقسم من XO_CONFIG أو من الملف') + '</div></div>'))
    # 15 WHAT IT'S MADE ME — proof without flexing
    facts = ''.join('<div class="fact rv"><b>' + a + '</b><span class="mut">' + b + '</span></div>' for a, b in d['facts'])
    s.append(band('dark', '<div class="c narrow rv"><h2>' + d['made_h2'] + '</h2><p class="lead mut">' + d['made_p'] + '</p></div>'
                  '<div class="facts">' + facts + '</div>' + cta()))
    # 16 SMALL-AUDIENCE CASE
    s.append(band('light', '<div class="narrow rv"><span class="eye">' + d['case_eye'] + '</span><h2>' + d['case_h2'] + '</h2>'
                  '<div class="ph" style="margin-top:20px">' + R(d['case_ph']) + '</div>'
                  '<p class="mut" style="margin-top:12px;font-size:14px">' + d['case_disc'] + '</p></div>'))
    # 17 THE MATH
    mt = ''.join('<div class="mt rv"><h3>' + a + '</h3><p class="eq">' + b + '</p><p class="res">' + c + '</p></div>' for a, b, c in d['math'])
    s.append(band('soft', '<div class="c narrow rv"><span class="eye">الحسبة</span><h2>' + d['math_h2'] + '</h2></div>'
                  '<div class="math">' + mt + '</div><p class="mut c" style="margin-top:16px;font-size:14px">تقدير مش وعد. الأرقام أمثلة، وإنت بتحط أرقامك.</p>'))
    # 18 VALUE STACK SUMMARY
    rows = ''.join('<div class="row"><span>' + a + '</span><span>' + b + '</span></div>' for a, b in d['sum_rows'])
    s.append(band('brand', '<div class="c rv"><h2>' + d['sum_h2'] + '</h2></div><div class="sum rv">' + rows +
                  '<div class="row tot"><span>القيمة الإجمالية</span><span>' + d['sum_total'] + '</span></div>'
                  '<div class="row now"><span>سعر التذكرة اليوم</span><span class="mono" data-price></span></div></div>'
                  '<p class="c mut" style="margin-top:14px">' + d['sum_honest'] + '</p>' + cta(), id_='xo-offer'))
    # 19 RESULTS WALL
    wall = ''.join('<div class="ph rv">' + R('سكرين شوت حقيقي ' + str(i + 1) + ' مع تظليل السطر المهم') + '</div>' for i in range(6))
    s.append(band('soft', '<div class="c narrow rv"><span class="eye">نتائج</span><h2>' + d['wall_h2'] + '</h2></div><div class="wall">' + wall + '</div>'
                  '<p class="mut c" style="margin-top:14px;font-size:14px">النتائج مش نموذجية ومش مضمونة. الخيط المشترك: ' + R('شو عملوا كلهم') + '</p>'))
    # 20 PRICE STORY + SCARCITY
    s.append(band('dark', '<div class="c narrow rv"><h2>' + d['scar_h2'] + '</h2><p class="lead mut">' + d['scar_p'] + '</p>'
                  '<div class="seats">' + d['seats'] + '</div>' + countdown() + '</div>'))
    # 21 CONDITIONAL GUARANTEE
    s.append(band('soft', '<div class="gu rv"><div class="seal"><div>' + d['seal'] + '</div></div><div><h2 style="font-size:clamp(24px,3.4vw,36px)">' + d['gu_h2'] + '</h2>'
                  '<p class="lead mut">' + d['gu_p'] + '</p></div></div>'))
    # 22 NOT FOR / IS FOR
    nots = ''.join('<div class="rv">' + n + '</div>' for n in d['notfor'])
    s.append(band('dark', '<div class="c rv"><h2>هالورشة مش إلك إذا…</h2></div><div class="not">' + nots + '</div>'
                  '<p class="is rv">' + d['isfor'] + '</p>' + cta()))
    # 23 TESTIMONIALS
    tg = ''.join('<div class="ph rv">' + R(t) + '</div>' for t in ['قصة فيديو حقيقية 1', 'قصة فيديو حقيقية 2', 'اقتباس حقيقي مع الاسم والمحل'])
    s.append(band('brand', '<div class="c rv"><h2>' + d['testi_h2'] + '</h2></div><div class="tg">' + tg + '</div>'))
    # 24 FAQ
    faq = ''.join('<details><summary>' + q + '</summary><p>' + a + '</p></details>' for q, a in d['faq'])
    s.append(band('dark', '<div class="narrow"><div class="c rv"><span class="eye" style="background:rgba(255,255,255,.12)">قبل ما تحجز</span><h2>الأسئلة اللي بتيجينا</h2></div>'
                  '<div class="faq">' + faq + '</div>' + cta() + '</div>'))
    # 25 LAST THING
    letter = ''.join('<p>' + p + '</p>' for p in d['letter'])
    s.append(band('dark', '<div class="last"><div class="pols rv"><div class="pol"><div class="ph">' + R('صورة حقيقية 1') + '</div>' + d['pol'][0] + '</div>'
                  '<div class="pol"><div class="ph">' + R('صورة حقيقية 2') + '</div>' + d['pol'][1] + '</div></div>'
                  '<div class="letter rv"><span class="eye" style="background:rgba(255,255,255,.12);justify-self:start">شغلة أخيرة</span>' + letter +
                  '<p class="sig">' + d['sig'] + '</p></div></div>' + cta(d['final_sub']) +
                  '<p class="ps narrow"><b>P.S.</b> ' + d['ps'] + '</p>', cls='lastb'))
    s.append('<footer class="foot"><div class="in"><span>' + d['brand'] + '</span><span>الشروط</span><span>الخصوصية</span><span>سياسة الاسترداد</span><span>الدعم: ' + R('رقم أو إيميل الدعم') + '</span></div></footer>')
    return s
