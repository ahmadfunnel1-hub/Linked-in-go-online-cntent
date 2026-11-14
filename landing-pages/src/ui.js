<script>
(function () {
  var cfg = window.LP_CONFIG, root = document.querySelector('.isl-lp');
  function track(e, d) { try { window.dataLayer.push(Object.assign({ event: e, campaign: cfg.campaign }, d || {})); } catch (x) {} }
  function $all(sel, el) { return [].slice.call((el || root).querySelectorAll(sel)); }

  $all('.isl-cover-src').forEach(function (i) { if (cfg.ebookCoverUrl) i.src = cfg.ebookCoverUrl; });
  $all('.isl-logo-light').forEach(function (i) { if (cfg.logoOnLightUrl) i.src = cfg.logoOnLightUrl; });

  // Tickable cards with a result box (data-r on .isl-result = JSON [[title, body, button], ...] indexed by number ticked)
  var res = root.querySelector('.isl-result[data-r]');
  if (res) {
    var R = JSON.parse(res.getAttribute('data-r')), pains = $all('.isl-pain');
    pains.forEach(function (c) { c.addEventListener('click', function () {
      var on = c.classList.toggle('isl-on'); c.setAttribute('aria-pressed', on);
      var n = $all('.isl-pain.isl-on').length;
      res.classList.toggle('isl-has', n > 0);
      $all('.isl-meter i', res).forEach(function (b, i) { b.classList.toggle('isl-lit', i < n); });
      res.querySelector('.isl-r-title').textContent = R[n][0];
      res.querySelector('.isl-r-body').textContent = R[n][1];
      if (R[n][2]) res.querySelector('.isl-r-cta').textContent = R[n][2];
      track('self_check', { ticked: n });
    }); });
  }

  // Flip cards
  $all('.isl-myth').forEach(function (m) {
    $all('.isl-flip-btn', m).forEach(function (b) { b.addEventListener('click', function () {
      var f = m.classList.toggle('isl-flip');
      m.querySelector('.isl-front').setAttribute('aria-hidden', f); m.querySelector('.isl-back').setAttribute('aria-hidden', !f);
    }); });
  });

  // Chat-style FAQ
  var items = $all('.isl-qa');
  function setOpen(it, open) {
    var a = it.querySelector('.isl-a'), q = it.querySelector('.isl-q');
    if (open) { it.classList.add('isl-open'); q.setAttribute('aria-expanded', 'true'); a.style.height = a.scrollHeight + 'px'; setTimeout(function () { if (it.classList.contains('isl-open')) a.style.height = 'auto'; }, 420); }
    else { a.style.height = a.scrollHeight + 'px'; a.offsetHeight; it.classList.remove('isl-open'); q.setAttribute('aria-expanded', 'false'); a.style.height = '0px'; }
  }
  items.forEach(function (it) {
    it.querySelector('.isl-a').style.height = it.classList.contains('isl-open') ? 'auto' : '0px';
    it.querySelector('.isl-q').addEventListener('click', function () {
      var will = !it.classList.contains('isl-open');
      items.forEach(function (o) { if (o !== it && o.classList.contains('isl-open')) setOpen(o, false); });
      setOpen(it, will);
    });
  });

  // Tabs
  $all('[data-tabs]').forEach(function (w) {
    var tabs = $all('.isl-tab', w), panels = $all('.isl-panel', w);
    function show(i) { tabs.forEach(function (t, j) { t.classList.toggle('isl-on', i === j); t.setAttribute('aria-selected', i === j); }); panels.forEach(function (p, j) { p.classList.toggle('isl-on', i === j); }); }
    tabs.forEach(function (t, i) { t.addEventListener('click', function () { show(i); track('tab_view', { label: t.textContent.trim() }); }); });
    show(0);
  });

  // On/off switch that changes a diagram or message (data-switch)
  $all('[data-switch]').forEach(function (w) {
    var b = w.querySelector('.isl-switch'), m = w.querySelector('.isl-flow-msg');
    b.addEventListener('click', function () {
      var on = w.classList.toggle('isl-on'); b.setAttribute('aria-checked', on);
      if (m) m.textContent = on ? m.getAttribute('data-on') : m.getAttribute('data-off');
      track('flow_switch', { on: on });
    });
  });

  // Hero demo buttons (data-demo): toggle isl-on on the target
  $all('[data-demo]').forEach(function (btn) {
    var t = root.querySelector(btn.getAttribute('data-demo')), m = t.querySelector('[data-msg]');
    btn.addEventListener('click', function () {
      var on = t.classList.toggle('isl-on');
      btn.textContent = on ? btn.getAttribute('data-label-on') : btn.getAttribute('data-label-off');
      if (m) m.textContent = on ? m.getAttribute('data-on') : m.getAttribute('data-off');
      track('hero_demo', { on: on });
    });
  });

  // Cost ledger (rows with switches) + summary
  $all('[data-ledger]').forEach(function (w) {
    var M = JSON.parse(w.getAttribute('data-ledger')), rows = $all('.isl-led-row', w), sum = w.querySelector('.isl-led-sum p');
    rows.forEach(function (r) { var s = r.querySelector('.isl-switch'); s.addEventListener('click', function () {
      var on = r.classList.toggle('isl-on'); s.setAttribute('aria-checked', on);
      r.querySelector('.isl-led-state').textContent = on ? 'We pay this' : 'Tick if you do';
      var n = $all('.isl-led-row.isl-on', w).length; sum.innerHTML = M[n]; track('ledger', { ticked: n });
    }); });
  });

  // Ring checklist
  $all('[data-ring]').forEach(function (w) {
    var M = JSON.parse(w.getAttribute('data-ring')), it = $all('.isl-rc-item', w), fg = w.querySelector('.isl-ring-fg'), num = w.querySelector('.isl-ring-c b'), msg = w.querySelector('.isl-rc-msg');
    it.forEach(function (b) { b.addEventListener('click', function () {
      b.classList.toggle('isl-on'); b.setAttribute('aria-pressed', b.classList.contains('isl-on'));
      var n = $all('.isl-rc-item.isl-on', w).length;
      fg.style.strokeDashoffset = 565 - 565 * n / it.length; num.textContent = n; msg.textContent = M[n]; track('ring_check', { ticked: n });
    }); });
  });

  // Radio cards
  $all('[data-radios]').forEach(function (w) {
    var rs = $all('.isl-radio', w), out = w.querySelector('.isl-radio-out'), p = out.querySelector('p');
    rs.forEach(function (r) { r.addEventListener('click', function () {
      rs.forEach(function (x) { x.classList.remove('isl-on'); x.setAttribute('aria-checked', 'false'); });
      r.classList.add('isl-on'); r.setAttribute('aria-checked', 'true');
      p.innerHTML = r.getAttribute('data-msg'); out.style.display = 'flex'; track('stage_pick', { stage: r.getAttribute('data-k') });
    }); });
  });

  // Readiness check (Yes / Not sure per row)
  $all('[data-ready]').forEach(function (w) {
    var M = JSON.parse(w.getAttribute('data-ready')), qs = $all('.isl-rq', w), out = w.querySelector('.isl-rout'), t = out.querySelector('b'), p = out.querySelector('span');
    qs.forEach(function (q) { $all('button', q).forEach(function (b) { b.addEventListener('click', function () {
      $all('button', q).forEach(function (x) { x.classList.remove('isl-on'); x.setAttribute('aria-pressed', 'false'); });
      b.classList.add('isl-on'); b.setAttribute('aria-pressed', 'true');
      var answered = $all('button.isl-on', w).length, yes = $all('button.isl-yes.isl-on', w).length;
      if (answered === qs.length) { out.style.display = 'flex'; t.textContent = M[yes][0]; p.textContent = M[yes][1]; track('readiness', { yes: yes }); }
    }); }); });
  });

  // Reveal on scroll + progress bars
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('isl-in'); io.unobserve(e.target); } }); }, { threshold: .15 });
    $all('.isl-rv, .isl-bar').forEach(function (el) { io.observe(el); });
  } else { $all('.isl-rv, .isl-bar').forEach(function (el) { el.classList.add('isl-in'); }); }

  // Mobile sticky CTA: shown after the hero, hidden while the form is on screen
  var sticky = root.querySelector('.isl-sticky'), hero = root.querySelector('.isl-hero'), dl = document.getElementById('isl-download');
  if (sticky && hero && dl) {
    var upd = function () {
      var past = hero.getBoundingClientRect().bottom < 0, r = dl.getBoundingClientRect(), on = r.top < innerHeight && r.bottom > 0;
      sticky.classList.toggle('isl-show', past && !on);
    };
    addEventListener('scroll', upd, { passive: true }); upd();
  }
})();
</script>
