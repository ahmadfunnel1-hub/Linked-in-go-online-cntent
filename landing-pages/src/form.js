<script>
(function () {
  var cfg = window.LP_CONFIG;

  // In-page links scroll smoothly without changing the URL (safe inside GHL page builders).
  document.querySelectorAll('.isl-lp a[href^="#isl-"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var t = document.getElementById(a.getAttribute('href').slice(1));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });
  function hostOf(url) { try { return new URL(url, location.href).hostname; } catch (e) { return ''; } }
  function track(event, data) { window.dataLayer.push(Object.assign({ event: event, campaign: cfg.campaign }, data || {})); }


  // Brand assets from LP_CONFIG
  (function () {
    var brand = document.querySelector('.isl-lp .isl-brand');
    var hero = document.querySelector('.isl-lp .isl-hero');
    if (hero && cfg.heroImageUrl) {
      var light = hero.classList.contains('isl-hero-light');
      var veil = light ? 'linear-gradient(90deg, rgba(255,255,255,.96) 0%, rgba(255,255,255,.88) 55%, rgba(255,255,255,.55) 100%)'
                       : 'linear-gradient(90deg, rgba(19,33,70,.96) 0%, rgba(19,33,70,.85) 55%, rgba(19,33,70,.55) 100%)';
      hero.style.backgroundImage = veil + ', url("' + cfg.heroImageUrl + '")';
      hero.classList.add('isl-has-photo');
    }
  })();
  document.querySelectorAll('.isl-lp .isl-logo-dark').forEach(function (i) { if (cfg.logoUrl) i.src = cfg.logoUrl; });
  document.querySelectorAll('.isl-lp .isl-logo-light').forEach(function (i) { if (cfg.logoOnLightUrl) i.src = cfg.logoOnLightUrl; });
  document.querySelector('.isl-yr').textContent = new Date().getFullYear();
  document.querySelectorAll('.isl-privacy-link').forEach(function (a) { a.href = cfg.privacyUrl; });
  document.querySelectorAll('.isl-ebook-link').forEach(function (a) { a.href = cfg.ebookUrl; });
  if (cfg.ebookCoverUrl) {
    var mock = document.querySelector('.isl-cover');
    if (mock) { var img = document.createElement('img');
    img.src = cfg.ebookCoverUrl; img.alt = mock.getAttribute('aria-label'); img.className = 'isl-cover-img';
    mock.replaceWith(img); }
  }

  // UTM / source attribution.
  var params = new URLSearchParams(location.search);
  var utm = {};
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(function (k) { if (params.get(k)) utm[k] = params.get(k); });
  track('page_view', utm);

  document.querySelectorAll('.isl-lp [data-cta]').forEach(function (el) {
    el.addEventListener('click', function () {
      track('ebook_cta_click', { position: el.dataset.cta });
      setTimeout(function () { document.getElementById('isl-fullName').focus({ preventScroll: true }); }, 500);
    });
  });

  var freeDomains = /@(gmail|googlemail|yahoo|hotmail|outlook|live|msn|icloud|me|aol|proton|protonmail|gmx|mail|yandex)\./i;
  var form = document.querySelector('form.isl-lead-form');
  var started = false;
  form.addEventListener('input', function () { if (!started) { started = true; track('form_start'); } });

  function validate() {
    var ok = true;
    form.querySelectorAll('.isl-field').forEach(function (f) {
      var input = f.querySelector('input, select');
      var v = input.value.trim();
      var bad = !v;
      if (input.type === 'email') bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || freeDomains.test(v);
      f.classList.toggle('isl-invalid', bad);
      if (bad) ok = false;
    });
    return ok;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    form.querySelector('.isl-form-error').style.display = 'none';
    if (!validate()) {
      track('form_error');
      var first = form.querySelector('.isl-invalid input, .isl-invalid select');
      if (first) first.focus();
      return;
    }
    var data = Object.fromEntries(new FormData(form).entries());
    data.marketingConsent = data.marketingConsent === 'yes';
    data.marketingConsentText = data.marketingConsent ? form.querySelector('.isl-consent').innerText.replace(/^Optional\s*/i, '').replace(/\s*You don.t need to tick this.*$/i, '').trim() : '';
    data.privacyNoticeUrl = cfg.privacyUrl;
    data.submittedAt = new Date().toISOString();
    data.campaign = cfg.campaign;
    data.page = location.href.split('?')[0];
    Object.assign(data, utm);

    // Open the download tab inside the click, so browsers don't treat it as a pop-up.
    var hasEbook = cfg.ebookUrl && cfg.ebookUrl !== '#';
    var win = hasEbook ? window.open('', '_blank') : null;
    if (win) win.opener = null;

    var btn = form.querySelector('button[type=submit]');
    btn.disabled = true; btn.textContent = 'Sending…';

    var ghl = cfg.formMode === 'ghl' || (cfg.formMode !== 'json' && /(^|\.)leadconnectorhq\.com$/i.test(hostOf(cfg.formEndpoint)));
    var send;
    if (cfg.ghlFormId) {
      // Send to the native GHL form. Multipart is a "simple" request, so no CORS preflight is needed.
      var fd = {
        full_name: data.fullName || '', email: data.email || '', organization: data.company || '',
        ZQSKktjkyPL8h8JLjqk3: data.jobTitle || '',            // Job Title
        l2FumkrB0rpHrSHruNzh: data.companySize || '',         // Company Size
        X8NvXbldFGtIpNbvipxu: data.marketingConsent ? 'Yes' : 'No', // Marketing Consent
        zQAmA2lQlOLlGMLiWJCd: data.marketingConsentText || '', // Marketing Consent Text
        dCkNYTc8Wo9Mud4MfbrF: data.submittedAt,               // Consent Timestamp
        lWDeYsbE6TOEhFrNSpwQ: data.campaign,                  // Lead Campaign
        atWbpAcyPhNN0VzEEE2B: data.page,                      // Lead Source Page
        formId: cfg.ghlFormId, location_id: cfg.ghlLocationId,
        eventData: { source: 'direct', page: { url: location.href, title: document.title }, url_params: utm, campaign: cfg.campaign, referrer: document.referrer },
        sessionId: String(Date.now()), Timezone: 'Asia/Riyadh'
      };
      var mp = new FormData();
      mp.append('formData', JSON.stringify(fd));
      mp.append('locationId', cfg.ghlLocationId);
      mp.append('formId', cfg.ghlFormId);
      send = fetch('https://backend.leadconnectorhq.com/forms/submit', { method: 'POST', mode: 'no-cors', body: mp });
    } else if (!cfg.formEndpoint) {
      send = Promise.resolve();
    } else if (ghl) {
      // GHL inbound webhooks don't answer browser CORS checks, so send a form-encoded "simple" request.
      // The response can't be read in no-cors mode; a network failure still rejects.
      var body = new URLSearchParams();
      Object.keys(data).forEach(function (k) { body.append(k, String(data[k])); });
      send = fetch(cfg.formEndpoint, { method: 'POST', mode: 'no-cors', body: body });
    } else {
      send = fetch(cfg.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); });
    }

    send.then(function () {
      track('form_submit_success');
      form.querySelector('.isl-form-body').style.display = 'none';
      form.querySelector('.isl-success').style.display = 'block';
      track('thank_you_view');
      if (win) {
        win.location.href = cfg.ebookUrl;
        track('resource_download_success');
      }
      if (cfg.thankYouUrl) {
        try { sessionStorage.setItem('isl_first_name', (data.fullName || '').split(' ')[0]); } catch (e) {}
        setTimeout(function () { location.href = cfg.thankYouUrl; }, 400);
      }
    }).catch(function () {
      if (win) win.close();
      form.querySelector('.isl-form-error').style.display = 'block';
      btn.disabled = false; btn.textContent = '__SEND__';
    });
  });

  form.querySelector('.isl-success .isl-ebook-link').addEventListener('click', function () { track('resource_download_success', { via: 'button' }); });
})();
</script>