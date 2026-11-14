from components import *

BOOKING = 'https://api.leadconnectorhq.com/widget/booking/KviFQud0pugnniFvoVHt'
PRISM = 'https://assets.cdn.filesafe.space/vhJRhZJvL4LvDBJd7NM0/media/dc63e9ca-1cbd-4e2e-98c1-e00b9ecd7c3a.webp'
MAZE = 'https://assets.cdn.filesafe.space/vhJRhZJvL4LvDBJd7NM0/media/e1457bb8-e1de-4e03-a320-27210bbd34bb.webp'

def ty_cfg(campaign, extra=''):
    return f'''<script>
  // Configure before launch.
  window.LP_CONFIG = {{
    campaign: "{campaign}",
    // GHL calendar embedded in step 2 (Calendars > Intrasoft). It must offer Sunday to Thursday.
    bookingUrl: "{BOOKING}",
    // Optional WhatsApp / email link shown under the calendar.
    contactUrl: "",
    logoUrl: "{LOGO_DARK}",
    logoOnLightUrl: "{LOGO_LIGHT}",
    privacyUrl: "#"{extra}
  }};
  window.dataLayer = window.dataLayer || [];
</script>'''

TY_JS = '''<script>
(function () {
  var cfg = window.LP_CONFIG, root = document.querySelector('.isl-lp');
  function track(e, d) { try { window.dataLayer.push(Object.assign({ event: e, campaign: cfg.campaign }, d || {})); } catch (x) {} }
  function set(sel, html) { var el = root.querySelector(sel); if (el && html) el.innerHTML = html; }
  track('thank_you_page_view');
  [].forEach.call(root.querySelectorAll('.isl-logo-dark'), function (i) { if (cfg.logoUrl) i.src = cfg.logoUrl; });
  [].forEach.call(root.querySelectorAll('.isl-logo-light'), function (i) { if (cfg.logoOnLightUrl) i.src = cfg.logoOnLightUrl; });
  root.querySelector('.isl-yr').textContent = new Date().getFullYear();
  [].forEach.call(root.querySelectorAll('.isl-privacy-link'), function (a) { a.href = cfg.privacyUrl; });
  var qs = location.search, isAI = /[?&]for=ai\\b/.test(qs), isImp = /[?&]ebook=impactful\\b/.test(qs), calTitle = root.getAttribute('data-cal') || 'Book your free review', reqText = root.getAttribute('data-req') || 'Request your free review';
  /*VARIANTS*/
  try {
    var first = sessionStorage.getItem('isl_first_name');
    if (first) { root.querySelector('.isl-name').textContent = first.replace(/[<>]/g, '') + ', '; var t = root.querySelector('.isl-h1t'); t.textContent = t.textContent.charAt(0).toLowerCase() + t.textContent.slice(1); }
  } catch (e) {}
  var cal = root.querySelector('.isl-cal'), alt = root.querySelector('.isl-alt');
  var bookUrl = (isAI && cfg.bookingUrlAi) ? cfg.bookingUrlAi : cfg.bookingUrl;
  if (bookUrl) {
    var f = document.createElement('iframe'); f.src = bookUrl; f.title = calTitle; f.loading = 'lazy'; cal.appendChild(f);
    if (cfg.contactUrl) alt.innerHTML = 'Prefer to message us? <a href="' + cfg.contactUrl + '" target="_blank" rel="noopener" data-cta="contact">Contact the Intrasoft team</a>';
  } else if (cfg.contactUrl) {
    cal.innerHTML = '<a class="isl-btn isl-btn-primary" href="' + cfg.contactUrl + '" target="_blank" rel="noopener" data-cta="contact">' + reqText + '</a>';
  } else { cal.innerHTML = '<p class="isl-note">The Intrasoft team will contact you shortly to arrange a time.</p>'; }
  root.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-cta]'); if (!a) return;
    track('cta_click', { position: a.getAttribute('data-cta') });
    if (a.getAttribute('href') === '#isl-next') { e.preventDefault(); document.getElementById('isl-next').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    if (a.getAttribute('data-cta') === 'contact') track('booking_request_click');
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('isl-in'); io.unobserve(e.target); } }); }, { threshold: .15 });
    [].forEach.call(root.querySelectorAll('.isl-rv'), function (el) { io.observe(el); });
  } else { [].forEach.call(root.querySelectorAll('.isl-rv'), function (el) { el.classList.add('isl-in'); }); }
})();
</script>
'''

def ty_body(*, h1, book_block, lead, cta, cover_html, steps3, next_eyebrow, next_h, next_lead, bullets, note, expect, tip, cal_title, req, step2_pill):
    bl = ''.join(f'<li><span class="isl-tk">✓</span><span><b>{b}</b> {r}</span></li>' for b, r in bullets)
    st = ''.join(f'<div class="isl-ns{" isl-done" if i == 0 else ""}"><i>{"✓" if i == 0 else i+1}</i><b>{b}</b><span>{s}</span></div>' for i, (b, s) in enumerate(steps3))
    ex = ''.join(f'<div class="isl-rv"><small>{a}</small><b>{b}</b><p>{c}</p></div>' for a, b, c in expect)
    check = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
    return f'''<div class="isl-lp" data-cal="{esc(cal_title)}" data-req="{esc(req)}">
<header class="isl-top"><div class="isl-wrap"><img class="isl-logo-dark" src="{LOGO_DARK}" alt="Intrasoft Middle East" width="82" height="40"></div></header>
<section class="isl-ty-hero">
  <div class="isl-wrap isl-ty-grid">
    <div>
      <div class="isl-tick-big">{check}</div>
      {eyebrow('Step 1 of 2 complete', 'isl-blue-e')}
      <h1><span class="isl-name"></span><span class="isl-h1t">{h1}</span></h1>
      {book_block}
      <p class="isl-lead">{lead}</p>
      <div class="isl-hero-ctas"><a class="isl-btn isl-btn-primary isl-cta-main" href="#isl-next" data-cta="to-next">{cta}</a></div>
      <p class="isl-cta-note">Your E-Book opened in a new tab, and a copy is on its way to your inbox. If you can't find the email, check your spam or promotions folder.</p>
      {lockup()}
    </div>
    <div class="isl-visual" aria-hidden="true">{cover_html}</div>
  </div>
  <div class="isl-wrap"><div class="isl-next3">{st}</div></div>
</section>
<section class="isl-pad isl-soft" id="isl-next">
  <div class="isl-wrap">
    <div class="isl-ty-book">
      <div class="isl-rv">
        {eyebrow(next_eyebrow)}
        <h2 class="isl-h2 isl-next-h" style="font-size:2.2rem">{next_h}</h2>
        <p class="isl-lead isl-next-lead">{next_lead}</p>
        <div class="isl-callout" style="margin-top:24px;border-left-color:var(--blue)"><div><p><b>In 30 minutes, we'll cover</b></p><ul class="isl-points isl-next-points">{bl}</ul></div></div>
        <p class="isl-fine" style="text-align:left;margin-top:16px">{note}</p>
      </div>
      <div class="isl-calcard isl-rv"><h3>Choose a time that suits you</h3><div class="isl-cal"></div><p class="isl-alt"></p></div>
    </div>
    <div class="isl-expect">{ex}</div>
    <div class="isl-tip isl-rv">{ico('book')}<p>{tip}</p></div>
  </div>
</section>
<footer class="isl-foot"><div class="isl-wrap"><span><b style="color:#fff">Intrasoft Middle East</b> · SAP Gold Partner · © <span class="isl-yr"></span> Intrasoft. SAP, the SAP logo, and the SAP partner logos are trademarks or registered trademarks of SAP SE or an SAP affiliated company in Germany and other countries.</span><span><a class="isl-privacy-link" href="#">Privacy notice</a></span></div></footer>
</div>
'''

EXPECT_GF = [('Before', 'Pick a time', 'Choose a 30-minute slot that suits you. The calendar shows Sunday to Thursday.'),
             ('During', 'A conversation, not a pitch', 'You speak with an Intrasoft SAP Cloud ERP consultant about your own business.'),
             ('After', 'No obligation', "No sales pressure: if GROW Fast isn't the right fit for you, we'll say so.")]

def ty_gf():
    cfg = ty_cfg('grow-fast-thank-you')
    cover_html = f'<img class="isl-ty-cover" src="{MAZE}" alt="SAP GROW Fast Myth Busting E-Book cover" width="260" height="316">'
    body = ty_body(h1='Your SAP GROW Fast Myth Busting E-Book is on its way.', book_block='',
                   lead='The E-Book answers the general questions. A free 30-minute fit check answers yours: whether GROW Fast suits your business, and what the commitment would look like.',
                   cta='Book your free fit check', cover_html=cover_html,
                   steps3=[('E-Book opened', 'In a new tab'), ('Check your inbox', 'A copy is on its way'), ('Book your fit check', 'Optional, free, 30 minutes')],
                   next_eyebrow='Step 2 · Optional, free, 30 minutes', next_h='Book your free GROW Fast fit check',
                   next_lead="The E-Book answers the general questions. A 30-minute fit check answers yours: whether GROW Fast suits your business, and what the commitment would look like.",
                   bullets=[('Your starting point:', 'current systems, spreadsheets and the priorities behind the move.'), ('What the predefined scope includes:', 'core finance, supply chain and HR best practices, and how they map to the way you work.'),
                            ('The commitment:', "how the SAP subscription and Intrasoft's implementation service are priced, and what affects them."), ('A realistic timeline:', 'what the target go-live depends on for a company like yours, and the next steps.')],
                   note="You'll speak with an Intrasoft SAP Cloud ERP consultant. No obligation and no sales pressure: if GROW Fast isn't the right fit for you, we'll say so.",
                   expect=EXPECT_GF, tip='<b>While you wait:</b> start with the myth that matches your biggest hesitation about SAP, whether that is cost, company size, time or complexity.',
                   cal_title='Book your free GROW Fast fit check', req='Request your GROW Fast fit check', step2_pill='')
    js = TY_JS.replace('/*VARIANTS*/', '')
    return page('Your SAP GROW Fast E-Book | Intrasoft', 'Your SAP GROW Fast Myth Busting E-Book is on its way. Book a free 30-minute fit check with Intrasoft.', cfg, body) + js, None

BDC_BOOK = 'Connect and Harmonize Business Data to Amplify the Power of AI'
def ty_bdc():
    cfg = ty_cfg('bdc-thank-you', ',\n    // Optional: cover image for "Driving Impactful Business Decisions" (shown when the link has ?ebook=impactful).\n    impactfulCoverUrl: "",\n    // Optional separate calendar for the data and AI readiness review (CIO / data leaders). Empty = same calendar.\n    bookingUrlAi: ""')
    cover_html = (f'<img class="isl-ty-cover" src="{PRISM}" alt="{BDC_BOOK} E-Book cover" width="260" height="316">'
                  + mock_cover('SAP Business Data Cloud', 'Driving impactful business decisions with <em>intelligent content</em>').replace('class="isl-mockcover"', 'class="isl-mockcover isl-ty-mock" style="display:none;margin:0 auto"'))
    book = f'<div class="isl-booktitle"><small>You requested</small><b class="isl-bt">{BDC_BOOK}</b></div>'
    body = ty_body(h1='Your SAP E-Book is on its way.', book_block=book,
                   lead='The E-Book shows why trusted, connected data comes first. A free 30-minute data review applies it to your own planning.', cta='Book your free data review', cover_html=cover_html,
                   steps3=[('E-Book opened', 'In a new tab'), ('Check your inbox', 'A copy is on its way'), ('Book a data review', 'Optional, free, 30 minutes')],
                   next_eyebrow='Step 2 · Optional, free, 30 minutes', next_h='Book your free finance planning data review',
                   next_lead='In 30 minutes, we look at where your planning and reporting slow down, and whether SAP Business Data Cloud and SAP Analytics Cloud could help.',
                   bullets=[('Where planning slows down:', 'the manual steps between your data and the forecast leadership sees.'), ('Your data sources:', 'which SAP and non-SAP systems feed your reports, and where definitions differ.'),
                            ('What could connect them:', 'how SAP Business Data Cloud and SAP Analytics Cloud could support your planning and scenarios.'), ('Sensible next steps:', 'what an assessment, scope and plan could involve.')],
                   note="You'll speak with an Intrasoft data and analytics consultant. No obligation and no sales pressure: if this approach isn't the right fit for you, we'll say so.",
                   expect=[('Before', 'Pick a time', 'Choose a 30-minute slot that suits you. The calendar shows Sunday to Thursday.'), ('During', 'A conversation, not a pitch', 'You speak with an Intrasoft data and analytics consultant about your own business.'), ('After', 'No obligation', "No sales pressure: if this approach isn't the right fit for you, we'll say so.")],
                   tip='<b>While you wait:</b> as you read, keep one question in mind: if leadership asked for a new scenario today, how much of the work would be finding and matching the data?',
                   cal_title='Book your finance planning data review', req='Request your finance planning data review', step2_pill='')
    variants = '''
  var V = { cal: calTitle, req: reqText };
  if (isImp) {
    root.querySelector('.isl-bt').textContent = 'Driving Impactful Business Decisions';
    set('.isl-lead', 'The E-Book shows how finance leaders turn business data into timely decisions. A free 30-minute data review applies it to your own finance planning.');
    var cv = root.querySelector('.isl-ty-cover'), mk = root.querySelector('.isl-ty-mock');
    if (cfg.impactfulCoverUrl) { cv.src = cfg.impactfulCoverUrl; cv.alt = 'Driving Impactful Business Decisions E-Book cover'; } else { cv.style.display = 'none'; mk.style.display = 'flex'; }
  }
  if (isAI) {
    set('.isl-lead', 'The E-Book shows why trusted, connected data comes first. A free 30-minute data and AI readiness review applies it to your own AI plans.');
    set('.isl-cta-main', 'Book your free data and AI readiness review');
    set('.isl-ns:nth-child(3) b', 'Book a readiness review');
    set('.isl-next-h', 'Book your free data and AI readiness review');
    set('.isl-next-lead', 'In 30 minutes, we look at how ready your business data is for AI, and where to start.');
    set('.isl-next-points',
      '<li><span class="isl-tk">✓</span><span><b>Where your data stands today:</b> quality, business context and access across your SAP and non-SAP systems.</span></li>' +
      '<li><span class="isl-tk">✓</span><span><b>Your AI plans:</b> which initiatives depend on connected, trusted data, and what has to come first.</span></li>' +
      '<li><span class="isl-tk">✓</span><span><b>What could connect it:</b> how SAP Business Data Cloud could support a reliable data foundation for AI.</span></li>' +
      '<li><span class="isl-tk">✓</span><span><b>Sensible next steps:</b> what an assessment, scope and plan could involve.</span></li>');
    calTitle = 'Book your data and AI readiness review'; reqText = 'Request your data and AI readiness review';
    track('thank_you_variant', { audience: 'ai' });
  }'''
    js = TY_JS.replace('/*VARIANTS*/', variants)
    return page('Your SAP Business Data Cloud E-Book | Intrasoft', 'Your SAP E-Book is on its way. Book a free 30-minute review with Intrasoft.', cfg, body) + js, None
