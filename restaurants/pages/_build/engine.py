"""Shared engine for the low-ticket live-workshop sales pages (25-section structure).
Every CSS rule is scoped under `.xo` so the page can be pasted into a GoHighLevel custom-code element.
Run:  python3 build.py   (writes ../<slug>.html, ../ghl-parts/<slug>-part-a.html / -part-b.html, ../../27-offer-pages-replace-list.md)
"""
import re, html as H

def R(s):
    """A visible placeholder for a fact the brief did not give. Never invent."""
    return '<span class="rp">[REPLACE: ' + s + ']</span>'

def cta(sub=''):
    s = '<div class="ctaw"><a class="cta" href="#xo-offer" data-cta><span data-cta-label></span> <span data-price></span></a>'
    if sub:
        s += '<p class="cta-sub">' + sub + '</p>'
    return s + '</div>'

def band(kind, inner, cls='', id_=''):
    idattr = ' id="' + id_ + '"' if id_ else ''
    return ('<section class="bd b-' + kind + (' ' + cls if cls else '') + '"' + idattr + '><div class="in">'
            + inner + '</div></section>')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={display}&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">')

CSS = r"""
/* Scoped under .xo so GoHighLevel styles never clash. Rhythm: dark → light → brand → dark → brand(offer+bonuses) → dark → brand(proof) → dark. */
.xo{--dark:%(dark)s;--dark2:%(dark2)s;--light:%(light)s;--paper:#FFFFFF;--ink:%(ink)s;--muted:%(muted)s;--brand:%(brand)s;--brand2:%(brand2)s;--brand-ink:#FFFFFF;
  --cta:%(cta)s;--cta-ink:%(cta_ink)s;--hl:%(hl)s;--line:%(line)s;--soft:%(soft)s;
  --display:%(display_stack)s;--body:'IBM Plex Sans Arabic',Tahoma,Arial,sans-serif;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;
  direction:rtl;text-align:right;font-family:var(--body);font-size:17px;line-height:1.8;color:var(--ink);background:var(--light);color-scheme:light;
  -webkit-font-smoothing:antialiased;overflow-x:hidden}
.xo *,.xo *::before,.xo *::after{box-sizing:border-box}
.xo h1,.xo h2,.xo h3,.xo h4,.xo p{margin:0}
.xo h1,.xo h2,.xo h3{font-family:var(--display);font-weight:800;line-height:1.3;text-wrap:balance;letter-spacing:0}
.xo h2{font-size:clamp(28px,4.6vw,48px)}
.xo h3{font-size:clamp(19px,2.2vw,23px);font-weight:700}
.xo a{color:inherit}
.xo img{max-width:100%%;display:block}
.xo .in{max-width:1120px;margin-inline:auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.xo .bd{padding-block:clamp(56px,8vw,96px)}
.xo .b-dark{background:var(--dark);color:#EEF2F1}
.xo .b-light{background:var(--paper);color:var(--ink)}
.xo .b-soft{background:var(--light);color:var(--ink)}
.xo .b-brand{background:var(--brand);color:var(--brand-ink)}
.xo .b-dark .mut,.xo .b-brand .mut{color:rgba(255,255,255,.78)}
.xo .mut{color:var(--muted)}
.xo .c{text-align:center}
.xo .narrow{max-width:780px;margin-inline:auto}
.xo .eye{display:inline-block;font-family:var(--display);font-weight:700;font-size:14px;letter-spacing:.02em;padding:5px 14px;border-radius:999px;background:rgba(127,127,127,.16);margin-bottom:16px}
.xo .hl{background:linear-gradient(transparent 55%%,var(--hl) 55%%);padding-inline:3px;color:inherit}
.xo .b-dark .hl,.xo .b-brand .hl{background:none;color:var(--cta)}
.xo .lead{font-size:clamp(17px,2vw,20px);margin-top:14px}
.xo .mono{font-family:var(--mono);font-variant-numeric:tabular-nums;direction:ltr;unicode-bidi:isolate}
.xo .rp{display:inline;background:#FFF0B8;color:#5A4300;border:1px dashed #C9A227;border-radius:6px;padding:0 6px;font-family:var(--body);font-weight:600;font-size:.86em;line-height:1.9}
.xo .ph{border:2px dashed rgba(127,127,127,.5);border-radius:18px;padding:22px;display:grid;gap:8px;place-items:center;text-align:center;min-height:140px;background:rgba(127,127,127,.06)}
/* CTA */
.xo .ctaw{display:grid;justify-items:center;gap:8px;margin-top:34px}
.xo .cta{display:inline-flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap;text-align:center;text-decoration:none;font-family:var(--display);font-weight:800;font-size:clamp(17px,2.1vw,21px);line-height:1.4;background:var(--cta);color:var(--cta-ink);padding:17px 30px;border-radius:14px;box-shadow:0 12px 0 -4px rgba(0,0,0,.18),0 18px 34px rgba(0,0,0,.18);transition:transform .15s ease,box-shadow .15s ease;max-width:100%%}
.xo .cta:hover{transform:translateY(-2px)}
.xo .cta:focus-visible,.xo button:focus-visible,.xo summary:focus-visible{outline:3px solid var(--cta);outline-offset:4px}
.xo .cta [data-price]{font-family:var(--mono);direction:ltr;unicode-bidi:isolate}
.xo .cta-sub{font-size:14px;opacity:.8}
/* 1 HERO */
.xo .hero{position:relative;background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,.78)),var(--hero-img,none) center/cover no-repeat,var(--dark);color:#fff;padding-block:clamp(60px,9vw,112px);overflow:hidden}
.xo .hero::after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 1px,transparent 1px);background-size:22px 22px;pointer-events:none}
.xo .hero .in{position:relative;z-index:1;display:grid;justify-items:center;text-align:center}
.xo .season{font-family:var(--display);font-weight:700;font-size:15px;color:var(--cta);border:1px solid rgba(255,255,255,.25);border-radius:999px;padding:5px 16px;margin-bottom:22px}
.xo .hero h1{font-size:clamp(34px,6vw,68px);max-width:16ch}
.xo .hero .lead{color:rgba(255,255,255,.82);max-width:640px}
.xo .when{display:flex;gap:10px 22px;flex-wrap:wrap;justify-content:center;margin-top:22px;font-size:15px;color:rgba(255,255,255,.85)}
.xo .when b{font-family:var(--display)}
.xo .cd{display:flex;gap:10px;justify-content:center;margin-top:22px}
.xo .cd div{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.16);border-radius:12px;min-width:68px;padding:8px 10px;text-align:center}
.xo .cd b{display:block;font-family:var(--mono);font-size:26px;line-height:1.2}
.xo .cd span{font-size:12px;opacity:.75}
/* 2 REFRAME */
.xo .reframe h2{font-size:clamp(30px,5.4vw,58px);max-width:20ch;margin-inline:auto}
/* 3 WEEK */
.xo .week{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start}
.xo .days{display:grid;gap:10px;margin-top:22px}
.xo .dy{display:grid;grid-template-columns:86px 1fr;gap:14px;align-items:start;background:var(--light);border-radius:14px;padding:12px 16px}
.xo .dy b{font-family:var(--display);color:var(--brand)}
.xo .story{background:var(--dark);color:#EEF2F1;border-radius:22px;padding:26px}
.xo .story .big{font-family:var(--mono);font-size:44px;color:var(--cta);line-height:1.1;margin-block:8px}
.xo .insight{margin-top:26px;font-family:var(--display);font-weight:800;font-size:clamp(20px,2.6vw,26px);border-right:5px solid var(--brand);padding-right:16px}
/* 4 ROLE */
.xo .role h2 s{text-decoration-thickness:4px;opacity:.7}
/* 5 GRID */
.xo .grid6{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:32px}
.xo .card{background:var(--paper);color:var(--ink);border-radius:18px;padding:22px;display:grid;gap:8px;align-content:start;border:1px solid var(--line)}
.xo .card .ic{width:48px;height:48px;border-radius:14px;background:var(--soft);display:grid;place-items:center;font-family:var(--mono);font-weight:600;color:var(--brand);font-size:15px}
.xo .card .t{font-family:var(--mono);font-size:13px;color:var(--muted)}
.xo .card.fun{background:var(--cta);color:var(--cta-ink);border-color:transparent}
.xo .card.fun .ic{background:rgba(0,0,0,.08);color:var(--cta-ink)}
.xo .sub6{margin-top:20px;font-family:var(--display);font-weight:700}
/* 6 TRUST */
.xo .vs{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:stretch;margin-top:30px}
.xo .vs .side{border-radius:18px;padding:22px;background:rgba(255,255,255,.12)}
.xo .vs .side.us{background:var(--paper);color:var(--ink)}
.xo .vs .x{display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:22px}
.xo .vs ul{margin:10px 0 0;padding:0 18px 0 0;display:grid;gap:6px;font-size:15.5px}
/* 7 DIFF */
.xo .meta{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px}
.xo .meta div{border:1px solid rgba(255,255,255,.18);border-radius:18px;padding:22px}
.xo .meta b{font-family:var(--display);font-size:19px;display:block;margin-bottom:6px}
.xo .stat{display:inline-grid;gap:2px;margin-top:26px;border-top:1px dashed rgba(255,255,255,.3);padding-top:18px}
.xo .stat b{font-family:var(--mono);font-size:clamp(38px,6vw,60px);color:var(--cta);line-height:1}
/* 8 INTRO */
.xo .intro .name{font-family:var(--display);font-weight:900;font-size:clamp(38px,7vw,84px);line-height:1.15;margin-block:10px}
.xo .intro .tagline{font-family:var(--display);font-weight:800;font-size:22px;margin-top:18px;color:var(--cta)}
/* 9-11 STACK */
.xo .item{display:grid;grid-template-columns:auto 1fr;gap:22px;background:var(--paper);color:var(--ink);border-radius:24px;padding:clamp(20px,3vw,34px);margin-top:22px;box-shadow:0 24px 50px rgba(0,0,0,.18)}
.xo .item .no{font-family:var(--mono);font-weight:600;font-size:15px;background:var(--dark);color:#fff;border-radius:12px;padding:8px 12px;height:max-content}
.xo .item h3{font-size:clamp(22px,3vw,30px)}
.xo .meta-row{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:10px;font-size:15px;color:var(--muted)}
.xo .meta-row b{color:var(--ink);font-family:var(--display)}
.xo .dd{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:18px}
.xo .dd div{background:var(--light);border-radius:16px;padding:16px;border-top:4px solid var(--brand)}
.xo .dd b{display:block;font-family:var(--display);font-size:16px}
.xo .dd .k{font-family:var(--mono);font-size:12.5px;color:var(--brand)}
.xo .val{margin-top:18px;font-family:var(--display);font-weight:800;font-size:18px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.xo .val .tag{background:var(--soft);color:var(--brand);border-radius:8px;padding:2px 10px;font-size:14px}
.xo .mini{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:18px}
.xo .mini div{border:1px solid var(--line);border-radius:14px;padding:14px;font-size:15px}
.xo .mini b{display:block;font-family:var(--display)}
.xo .promise{margin-top:16px;background:var(--soft);border-radius:16px;padding:16px 18px}
.xo .promise b{font-family:var(--display);color:var(--brand);display:block;margin-bottom:6px}
.xo .promise ul{margin:0;padding:0 18px 0 0;display:grid;gap:4px;font-size:15.5px}
/* 12 MARQUEE */
.xo .mq{background:var(--cta);color:var(--cta-ink);overflow:hidden;white-space:nowrap;border-block:3px solid var(--dark);padding-block:12px}
.xo .mq .tr{display:inline-flex;gap:28px;font-family:var(--display);font-weight:900;font-size:22px;animation:xo-mq 22s linear infinite}
@keyframes xo-mq{to{transform:translateX(50%%)}}
/* 13 BONUSES */
.xo .bonus{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.xo .bn{background:var(--paper);color:var(--ink);border-radius:22px;padding:24px;display:grid;gap:10px;align-content:start;position:relative}
.xo .bn .n{font-family:var(--mono);font-size:13px;color:var(--muted)}
.xo .bn .kills{font-family:var(--display);font-weight:700;font-size:14.5px;color:#B4231B;background:#FBE9E7;border-radius:10px;padding:6px 10px}
.xo .bn .kills s{text-decoration-thickness:2px}
/* 15 MADE */
.xo .facts{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.xo .fact{border-radius:18px;padding:22px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14)}
.xo .fact b{display:block;font-family:var(--mono);font-size:clamp(30px,4vw,42px);color:var(--cta);line-height:1.15}
/* 17 MATH */
.xo .math{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.xo .mt{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:22px;display:grid;gap:8px;align-content:start}
.xo .mt .eq{font-family:var(--mono);font-size:15px;background:var(--light);border-radius:10px;padding:8px 10px;direction:rtl}
.xo .mt .res{font-family:var(--display);font-weight:800;color:var(--brand)}
/* 18 SUMMARY */
.xo .sum{max-width:760px;margin:28px auto 0;background:var(--paper);color:var(--ink);border-radius:24px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.25)}
.xo .sum .row{display:flex;justify-content:space-between;gap:16px;padding:15px 22px;border-bottom:1px solid var(--line)}
.xo .sum .row span:last-child{font-family:var(--display);font-weight:700;white-space:nowrap}
.xo .sum .tot{background:var(--dark);color:#fff;font-family:var(--display);font-weight:800;font-size:19px}
.xo .sum .now{background:var(--soft);font-family:var(--display);font-weight:800;font-size:22px;color:var(--brand)}
/* 19 WALL */
.xo .wall{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:28px}
/* 20 SCARCITY */
.xo .seats{display:inline-flex;gap:10px;align-items:center;font-family:var(--display);font-weight:800;font-size:20px;background:rgba(255,255,255,.1);border-radius:999px;padding:8px 20px;margin-top:20px}
/* 21 GUARANTEE */
.xo .gu{display:grid;grid-template-columns:auto 1fr;gap:30px;align-items:center;background:var(--paper);color:var(--ink);border-radius:26px;padding:clamp(22px,4vw,40px);border:3px solid var(--cta)}
.xo .seal{width:150px;height:150px;border-radius:50%%;background:var(--cta);color:var(--cta-ink);display:grid;place-items:center;text-align:center;font-family:var(--display);font-weight:900;line-height:1.25;transform:rotate(-8deg)}
.xo .seal b{font-family:var(--mono);font-size:40px;display:block}
/* 22 FOR */
.xo .not{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:26px}
.xo .not div{background:rgba(255,255,255,.08);border-radius:16px;padding:16px 18px;font-size:16px}
.xo .not div::before{content:"✕ ";color:#FF8A80;font-weight:800}
.xo .is{margin-top:18px;background:var(--cta);color:var(--cta-ink);border-radius:18px;padding:18px 22px;font-family:var(--display);font-weight:800;font-size:clamp(18px,2.4vw,22px)}
/* 23 TESTI */
.xo .tg{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}
/* 24 FAQ */
.xo .faq{display:grid;gap:10px;margin-top:26px}
.xo details{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:0 20px}
.xo summary{cursor:pointer;list-style:none;font-family:var(--display);font-weight:700;font-size:17px;padding:17px 0;display:flex;justify-content:space-between;gap:12px}
.xo summary::-webkit-details-marker{display:none}
.xo summary::after{content:"+";font-family:var(--mono);font-size:24px;line-height:1;color:var(--cta)}
.xo details[open] summary::after{content:"–"}
.xo details p{padding-bottom:18px;color:rgba(255,255,255,.8)}
/* 25 LAST */
.xo .last{display:grid;grid-template-columns:.8fr 1.2fr;gap:40px;align-items:center}
.xo .pols{position:relative;height:340px}
.xo .pol{position:absolute;width:62%%;background:#fff;padding:10px 10px 36px;box-shadow:0 18px 40px rgba(0,0,0,.35);color:#333;font-size:13px;text-align:center}
.xo .pol .ph{min-height:170px;border-radius:4px;background:#EEE;color:#666}
.xo .pol:nth-child(1){top:0;right:0;transform:rotate(-6deg)}
.xo .pol:nth-child(2){bottom:0;left:0;transform:rotate(5deg)}
.xo .letter{display:grid;gap:14px;font-size:17.5px}
.xo .sig{font-family:var(--display);font-weight:800;font-size:22px;color:var(--cta)}
.xo .ps{margin-top:30px;border-top:1px dashed rgba(255,255,255,.3);padding-top:20px;font-size:16px;color:rgba(255,255,255,.85)}
.xo .ps b{font-family:var(--display);color:#fff}
.xo .foot{background:var(--dark2);color:rgba(255,255,255,.7);font-size:13.5px;padding-block:22px}
.xo .foot .in{display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:center}
/* sticky (mobile, after hero) */
.xo .sticky{position:fixed;left:0;right:0;bottom:0;z-index:999;background:var(--dark2);padding:10px max(16px,env(safe-area-inset-right,0px)) calc(10px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));display:none;transform:translateY(110%%);transition:transform .25s ease;box-shadow:0 -10px 30px rgba(0,0,0,.25)}
.xo .sticky .cta{width:100%%;padding:13px 18px;font-size:17px;box-shadow:none}
.xo .sticky.show{transform:none}
/* scroll reveal: content is visible at rest, only slides in */
.xo .rv{transition:transform .6s ease}
.xo .rv.pre{transform:translateY(26px)}
@media (max-width:900px){
  .xo .week,.xo .last{grid-template-columns:1fr}
  .xo .grid6,.xo .bonus,.xo .facts,.xo .math,.xo .wall,.xo .tg{grid-template-columns:1fr 1fr}
  .xo .dd,.xo .mini{grid-template-columns:1fr}
  .xo .vs{grid-template-columns:1fr}
  .xo .vs .x{padding:4px}
  .xo .gu{grid-template-columns:1fr;justify-items:center;text-align:center}
}
@media (max-width:768px){.xo .sticky{display:block}.xo{padding-bottom:76px}}
@media (max-width:560px){
  .xo .grid6,.xo .bonus,.xo .facts,.xo .math,.xo .wall,.xo .tg,.xo .meta,.xo .not{grid-template-columns:1fr}
  .xo .item{grid-template-columns:1fr}
  .xo .dy{grid-template-columns:1fr;gap:2px}
  .xo .pols{height:300px}
  .xo .cd div{min-width:58px}
}
@media (prefers-reduced-motion:reduce){.xo *{animation:none!important;transition:none!important}.xo .rv.pre{transform:none}}
"""

JS = r"""
<script>
(function(){
  var C = window.XO_CONFIG || {};
  var root = document.querySelector('.xo'); if(!root) return;
  var price = C.price || '[REPLACE: السعر]';
  root.querySelectorAll('[data-price]').forEach(function(e){ e.textContent = price; });
  root.querySelectorAll('[data-cta-label]').forEach(function(e){ e.textContent = C.ctaLabel || 'احجز مقعدك بـ'; });
  if (C.heroImage) { var h = root.querySelector('.hero'); if (h) h.style.setProperty('--hero-img', 'url("' + C.heroImage + '")'); }
  // CTA → GHL popup button by ID → checkout URL → scroll to the offer
  root.querySelectorAll('[data-cta]').forEach(function(a){
    a.addEventListener('click', function(ev){
      ev.preventDefault();
      var b = C.ghlButtonId && document.getElementById(C.ghlButtonId);
      if (b) { b.click(); return; }
      if (C.checkoutUrl) { window.location.href = C.checkoutUrl; return; }
      var o = document.getElementById('xo-offer'); if (o) o.scrollIntoView({behavior:'smooth', block:'start'});
    });
  });
  // count-up
  function countUp(el){
    var to = parseFloat(el.getAttribute('data-count')), dec = (el.getAttribute('data-count').split('.')[1]||'').length, pre = el.getAttribute('data-pre')||'', suf = el.getAttribute('data-suf')||'';
    var t0 = null, dur = 1200;
    function step(t){ if(!t0) t0=t; var p=Math.min(1,(t-t0)/dur); var v=to*(1-Math.pow(1-p,3)); el.textContent = pre + v.toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec}) + suf; if(p<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.remove('pre'); if(e.target.hasAttribute('data-count')) countUp(e.target); io.unobserve(e.target);} }); }, {rootMargin:'0px 0px -8% 0px'});
    root.querySelectorAll('.rv').forEach(function(el){ if (el.getBoundingClientRect().top > window.innerHeight) { el.classList.add('pre'); } io.observe(el); });
    root.querySelectorAll('[data-count]').forEach(function(el){ io.observe(el); });
  }
  // countdown to the event start (hidden when no date is set)
  var cds = root.querySelectorAll('[data-countdown]');
  if (C.eventStartISO && cds.length) {
    var end = new Date(C.eventStartISO).getTime();
    var tick = function(){ var d = Math.max(0, end - Date.now()), s = Math.floor(d/1000);
      var v = [Math.floor(s/86400), Math.floor(s%86400/3600), Math.floor(s%3600/60), s%60];
      cds.forEach(function(cd){ cd.querySelectorAll('b').forEach(function(b,i){ b.textContent = String(v[i]).padStart(2,'0'); }); }); };
    tick(); setInterval(tick, 1000);
  } else { cds.forEach(function(cd){ cd.hidden = true; }); }
  // sticky CTA after the hero
  var st = root.querySelector('.sticky'), hero = root.querySelector('.hero');
  if (st && hero && 'IntersectionObserver' in window) { new IntersectionObserver(function(e){ st.classList.toggle('show', !e[0].isIntersecting); }).observe(hero); }
  else if (st) st.classList.add('show');
})();
</script>
"""

def config_script(cfg):
    import json
    return '<script>window.XO_CONFIG = ' + json.dumps(cfg, ensure_ascii=False, indent=2) + ';</script>'

def countdown():
    return ('<div class="cd" data-countdown aria-label="الوقت المتبقي لبداية الورشة">'
            '<div><b>00</b><span>يوم</span></div><div><b>00</b><span>ساعة</span></div>'
            '<div><b>00</b><span>دقيقة</span></div><div><b>00</b><span>ثانية</span></div></div>')

def page(p, sections, part=None):
    css = CSS % p['theme']
    fonts = FONTS.format(display=p['font_query'])
    if part == 'a':
        secs = sections[:11]
    elif part == 'b':
        secs = sections[11:]
    else:
        secs = sections
    body = ''.join(secs)
    sticky = '<div class="sticky">' + cta() + '</div>'
    head = ''
    if part is None:
        head = ('<title>' + p['title'] + '</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
                '<style>body{margin:0;background:' + p['theme']['dark'] + '}</style>\n')
    return (head + fonts + '\n<style>' + css + '</style>\n'
            + '<!-- ' + p['title'] + (' · PART ' + part.upper() if part else '') + ' · edit XO_CONFIG below first -->\n'
            + config_script(p['config']) + '\n<div class="xo">' + body + sticky + '</div>\n' + JS)

def replaces(html_text):
    seen, out = set(), []
    for m in re.finditer(r'\[REPLACE: ([^\]]+)\]', html_text):
        s = H.unescape(m.group(1)).strip()
        if s not in seen:
            seen.add(s); out.append(s)
    return out
