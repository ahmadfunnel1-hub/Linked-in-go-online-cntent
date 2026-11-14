"""Shared building blocks for the long-form landing pages and thank-you pages.
Run build.py to regenerate every page in landing-pages/variants and landing-pages/thank-you."""
import os, json, html
HERE = os.path.dirname(os.path.abspath(__file__))
def read(n): return open(os.path.join(HERE, n)).read()
GP = read('gp.svg')
LOGO_DARK = 'https://files.leadconnectorhq.com/file/6af2d08730caaf80f6316eda/intrasoft-logo-white-official.png'
LOGO_LIGHT = 'https://files.leadconnectorhq.com/file/6af2d088923b4bc1094f29c0/intrasoft-logo-dark-official.png'
PARTNER_URL = 'https://www.sap.com/partners/profile/intrasoft-middle-east'
LOCATION_ID = 'vhJRhZJvL4LvDBJd7NM0'
# One native GHL form per product, so each product runs its own workflow, tags and emails.
FORM_IDS = {'grow-fast': 's4SEN1Q2Jc1jmF6CUy4A', 'bdc': 'AJ2Qa4FMs3ghxZVJRAAK'}  # "SAP GROW Fast E-Book Download", "SAP BDC E-Book Download"

_I = {
 'check': '<path d="M20 6L9 17l-5-5"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/>',
 'down': '<path d="M12 5v14M5 12l7 7 7-7"/>',
 'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/>',
 'bolt': '<path d="M13 2L3 14h9l-1 8 10-12h-9z"/>',
 'wrench': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 'warn': '<path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>',
 'grid': '<rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/>',
 'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 'card': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/>',
 'people': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 'cog': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
 'link': '<path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/>',
 'layers': '<path d="M12 2l10 6-10 6L2 8z"/><path d="M2 12l10 6 10-6M2 16l10 6 10-6"/>',
 'truck': '<rect x="1" y="6" width="14" height="11" rx="1"/><path d="M15 9h4l3 3v5h-7"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
 'factory': '<path d="M2 21V9l6 4V9l6 4V5h4v16z"/>',
 'sheet': '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M10 3v18"/>',
 'cloud': '<path d="M18 10a6 6 0 0 0-11.6-1.6A4.5 4.5 0 0 0 7 17h11a3.5 3.5 0 0 0 0-7z"/>',
}
def ico(n, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[n]}</svg>'
def esc(s): return html.escape(s, quote=True)
def jattr(o): return esc(json.dumps(o, ensure_ascii=False))

_gp_n = [0]
def lockup(light=False):
    _gp_n[0] += 1
    cls = 'isl-logo-light' if light else 'isl-logo-dark'
    logo = LOGO_LIGHT if light else LOGO_DARK
    gp = GP.replace('isl-gp-grad', f'isl-gp-grad{_gp_n[0]}')
    return (f'<div class="isl-lockup"><img class="{cls}" src="{logo}" alt="Intrasoft Middle East" width="131" height="64">'
            f'<a class="isl-gp" href="{PARTNER_URL}" target="_blank" rel="noopener" aria-label="Intrasoft Middle East on SAP Partner Finder">{gp}</a></div>')

def cfg_block(campaign, ebook_url, cover_url, thank_url):
    FORM_ID = FORM_IDS['grow-fast' if campaign.startswith('grow-fast') else 'bdc']
    return f'''<script>
  // Configure before launch.
  window.LP_CONFIG = {{
    campaign: "{campaign}",
    // Native GHL form for this product: submissions create the contact and fire "Form Submitted" for that form only.
    ghlFormId: "{FORM_ID}",
    ghlLocationId: "{LOCATION_ID}",
    formEndpoint: "",
    formMode: "auto",
    ebookUrl: "{ebook_url}",
    ebookCoverUrl: "{cover_url}",
    heroImageUrl: "",
    logoUrl: "{LOGO_DARK}",
    logoOnLightUrl: "{LOGO_LIGHT}",
    privacyUrl: "#",
    thankYouUrl: "{thank_url}"
  }};
  window.dataLayer = window.dataLayer || [];
</script>'''

def topbar(inner): return f'<div class="isl-topbar"><span class="isl-pulse"></span>{inner}</div>'
def header(btn):
    return (f'<header class="isl-top"><div class="isl-wrap"><img class="isl-logo-dark" src="{LOGO_DARK}" alt="Intrasoft Middle East" width="82" height="40">'
            f'<a class="isl-btn isl-btn-primary" href="#isl-download" data-cta="header">{btn}</a></div></header>')
def trust():
    items = [('shield', 'SAP Gold Partner'), ('clock', '26 years of regional presence'), ('chat', 'Arabic and English-speaking teams'), ('check', 'Support beyond go-live')]
    return '<div class="isl-trust"><div class="isl-wrap">' + ''.join(f'<span>{ico(i)}{t}</span>' for i, t in items) + '</div></div>'
def eyebrow(t, cls=''): return f'<p class="isl-eyebrow {cls}">{t}</p>'
def head(eyebrow_t, h2, lead=None, cls='isl-narrow isl-center isl-rv'):
    l = f'<p class="isl-lead">{lead}</p>' if lead else ''
    return f'<div class="{cls}">{eyebrow(eyebrow_t)}<h2 class="isl-h2">{h2}</h2>{l}</div>'
def g(t): return f'<span class="isl-grad">{t}</span>'
def section(inner, cls='isl-pad', sid=''):
    i = f' id="{sid}"' if sid else ''
    return f'<section class="{cls}"{i}><div class="isl-wrap">{inner}</div></section>'
def btn(text, href='#isl-download', cta='cta', primary=True, ghost=False, extra=''):
    c = 'isl-btn-ghost' if ghost else 'isl-btn-primary'
    return f'<a class="isl-btn {c}" href="{href}" data-cta="{cta}"{extra}>{text}</a>'

def mock_cover(small, title_html, tag='E-BOOK'):
    return f'<div class="isl-mockcover" role="img" aria-label="E-Book cover"><div><small>{small}</small><b>{title_html}</b></div><i>{tag}</i></div>'
def cover(cls, alt, mock=None):
    if mock: return mock
    return f'<img class="{cls} isl-cover-src" src="" alt="{esc(alt)}" width="260" height="316">'

def form_block(send, sub, ok_title):
    return f'''<form class="isl-lead-form" novalidate>
        <div class="isl-form-body">
          <h3>Get your free copy</h3>
          <p class="isl-sub">{sub}</p>
          <div class="isl-field"><label for="isl-fullName">Full name</label><input id="isl-fullName" name="fullName" autocomplete="name" required><div class="isl-error">Please enter your full name.</div></div>
          <div class="isl-field"><label for="isl-email">Business email</label><input id="isl-email" name="email" type="email" autocomplete="email" required><div class="isl-error">Please use a valid business email address.</div></div>
          <div class="isl-two">
            <div class="isl-field"><label for="isl-company">Company name</label><input id="isl-company" name="company" autocomplete="organization" required><div class="isl-error">Please enter your company name.</div></div>
            <div class="isl-field"><label for="isl-jobTitle">Job title</label><input id="isl-jobTitle" name="jobTitle" autocomplete="organization-title" required><div class="isl-error">Please enter your job title.</div></div>
          </div>
          <div class="isl-field"><label for="isl-companySize">Company size</label>
            <select id="isl-companySize" name="companySize" required>
              <option value="">Select…</option>
              <option>1–199 employees</option><option>200–999 employees</option><option>1,000–4,999 employees</option><option>5,000+ employees</option>
            </select><div class="isl-error">Please select your company size.</div></div>
          <label class="isl-consent"><input type="checkbox" name="marketingConsent" value="yes"><span><span class="isl-opt">Optional</span>Yes, Intrasoft may email me about SAP solutions, events and insights. I can unsubscribe at any time. You don't need to tick this to get the E-Book.</span></label>
          <p class="isl-privacy">By downloading, you acknowledge that Intrasoft will process your details to deliver this resource, as described in our <a class="isl-privacy-link" href="#">privacy notice</a>.</p>
          <button class="isl-btn isl-btn-primary" type="submit">{send}</button>
          <p class="isl-form-error" role="alert">Something went wrong. Please try again.</p>
          <div class="isl-safe"><span>{ico('lock')}Your details stay private</span><span>{ico('bolt')}Instant access</span></div>
        </div>
        <div class="isl-success" role="status">
          <div class="isl-big">✓</div>
          <h3>{ok_title}</h3>
          <p class="isl-sub">If it didn't open automatically, use the button below. We've also sent a copy to your inbox.</p>
          <a class="isl-btn isl-btn-primary isl-ebook-link" href="#" target="_blank" rel="noopener">Open the E-Book</a>
        </div>
      </form>'''

PIN = '<svg class="isl-pin" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="20" r="16" fill="#00A7E3"/><circle cx="19" cy="15" r="5" fill="#78DCFF" opacity=".8"/><path d="M24 36v10" stroke="#132146" stroke-width="3" stroke-linecap="round"/></svg>'

def convert(variant, *, book, cover_html, toc, eyebrow_t, send, sub, ok_title, h2=None, lead=None, chips=None, small_cover=None):
    """toc = list of (bold, rest). Variants: paper | center | split."""
    form = f'<div class="isl-form-card isl-rv">{form_block(send, sub, ok_title)}</div>'
    if variant == 'paper':
        lis = ''.join(f'<li><i>{n+1}</i><span><b>{b}</b> {r}</span></li>' for n, (b, r) in enumerate(toc))
        left = (f'<div class="isl-paper isl-rv">{PIN}<div class="isl-paper-head">{small_cover}<div><small>Free E-Book</small><h3>{book}</h3></div></div><ul class="isl-toc">{lis}</ul></div>')
        return f'<section class="isl-pad isl-convert" id="isl-download"><div class="isl-wrap isl-convert-grid">{left}{form}</div></section>'
    if variant == 'center':
        cs = ''.join(f'<span>{ico("check")}{c}</span>' for c in (chips or []))
        return (f'<section class="isl-pad isl-convert" id="isl-download"><div class="isl-wrap"><div class="isl-fc-head isl-rv">'
                f'<div class="isl-cover-wrap">{cover_html}</div>{eyebrow(eyebrow_t, "isl-blue-e")}<h2 class="isl-h2">{h2}</h2><p class="isl-lead">{lead}</p><div class="isl-fc-chips">{cs}</div></div>'
                f'<div class="isl-fc-form">{form}</div></div></section>')
    lis = ''.join(f'<li><i>{ico("check")}</i><span><b>{b}</b> {r}</span></li>' for b, r in toc).replace('<i><svg', '<i><svg width="12" height="12"')
    lis = ''.join(f'<li><i>✓</i><span><b>{b}</b> {r}</span></li>' for b, r in toc)
    left = (f'<div class="isl-split-cover isl-rv">{eyebrow(eyebrow_t, "isl-blue-e")}<h2 class="isl-h2" style="color:#fff">{h2}</h2>{cover_html}<ul class="isl-glass">{lis}</ul></div>')
    return f'<section class="isl-pad isl-convert" id="isl-download"><div class="isl-wrap isl-convert-grid">{left}{form}</div></section>'

def faq_chat(items, light_logo=LOGO_LIGHT):
    chev = '<svg class="isl-chev-i isl-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>'
    chev = chev.replace('isl-chev-i isl-chev', 'isl-chev')
    out = ''
    for i, (q, a) in enumerate(items):
        o = ' isl-open' if i == 0 else ''
        out += (f'<div class="isl-qa isl-rv{o}"><button class="isl-q" aria-expanded="{"true" if i == 0 else "false"}"><span class="isl-qm">?</span><span class="isl-qt">{q}</span>{chev}</button>'
                f'<div class="isl-a"><div class="isl-ar"><span class="isl-av" aria-hidden="true"><img class="isl-logo-light" src="{light_logo}" alt=""></span><div class="isl-bubble"><p>{a}</p></div></div></div></div>')
    return f'<div class="isl-chat">{out}</div>'
def faq_acc(items, one=False):
    out = ''.join(f'<details class="isl-det isl-rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'<div class="isl-acc{" isl-one" if one else ""}">{out}</div>'

def why_grid(items):
    return '<div class="isl-why">' + ''.join(f'<div class="isl-rv"><b>{t}</b><p>{p}</p></div>' for t, p in items) + '</div>'
def why_band(eyebrow_t, h2, lead, items, light=True):
    lis = ''.join(f'<li><i>{ico(ic)}</i><b>{t}</b><span>{p}</span></li>' for ic, t, p in items)
    return (f'<div class="isl-whyband"><div class="isl-rv">{eyebrow(eyebrow_t)}<h2 class="isl-h2">{h2}</h2><p class="isl-lead">{lead}</p>{lockup(light=True)}</div>'
            f'<ul class="isl-whylist isl-rv">{lis}</ul></div>')

def final(h2, p, send):
    return f'<section class="isl-final"><div class="isl-wrap"><h2>{h2}</h2><p>{p}</p>{btn(send, cta="final")}</div></section>'
def footer():
    return ('<footer class="isl-foot"><div class="isl-wrap"><span>© <span class="isl-yr"></span> Intrasoft. SAP, the SAP logo, and the SAP partner logos are trademarks or registered '
            'trademarks of SAP SE or an SAP affiliated company in Germany and other countries.</span><span><a class="isl-privacy-link" href="#">Privacy notice</a></span></div></footer>')
def sticky(text): return f'<div class="isl-sticky"><a class="isl-btn isl-btn-primary" href="#isl-download" data-cta="sticky">{text}</a></div>'

def flip_cards(cards, front_tag, back_tag, back_btn='Back', front_btn='See the answer'):
    arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg>'
    out = ''
    for i, (q, a) in enumerate(cards):
        out += (f'<div class="isl-myth isl-rv"><div class="isl-myth-in"><div class="isl-face isl-front"><span class="isl-tag">{front_tag.format(n=i+1)}</span><q>{q}</q>'
                f'<button type="button" class="isl-flip-btn">{front_btn} {arrow}</button></div><div class="isl-face isl-back" aria-hidden="true"><span class="isl-tag">{back_tag}</span><p>{a}</p>'
                f'<button type="button" class="isl-flip-btn">{back_btn} {arrow}</button></div></div></div>')
    return out

def tabs(items, dark=False):
    """items = [(label, panel_html)]"""
    tl = ''.join(f'<button class="isl-tab" role="tab" type="button">{l}</button>' for l, _ in items)
    pn = ''.join(f'<div class="isl-panel" role="tabpanel">{p}</div>' for _, p in items)
    return f'<div class="isl-tabs isl-rv" data-tabs><div class="isl-tablist" role="tablist">{tl}</div>{pn}</div>'

def page(title, desc, cfg, body):
    css = read('kit.css') + read('kit2.css')
    return (f'<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n'
            f'<meta name="description" content="{esc(desc)}">\n'
            '<!--\n  Paste this WHOLE file into a GoHighLevel "Custom JS/HTML" element.\n  - Set the GHL section and row to full width with zero padding.\n'
            '  - All classes and IDs start with isl- so they cannot clash with GHL.\n  - Settings (form, E-Book PDF, cover, privacy link, thank-you page) are in LP_CONFIG below.\n  - Source: landing-pages/src (run build.py to regenerate).\n-->\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">\n'
            f'<style>\n{css}\n</style>\n\n{cfg}\n\n<div class="isl-lp">\n{body}\n</div>\n\n')
