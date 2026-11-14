"""Builds the branded HTML emails from the nurture copy (*.md in this folder).

Usage:  python3 build_emails.py OUT_DIR
Writes OUT_DIR/<product>-<id>.html and OUT_DIR/index.json (title, subject, alt subject, preview, file).
Paste/push each file into the matching GHL email template (see ghl-workflow-notes.md).

Brand rules applied (SAP Gold Partner guideline + Intrasoft feedback):
- Header: Intrasoft logo only. Footer: Intrasoft logo + SAP Gold Partner logo side by side, no divider,
  SAP logo 96px wide (min 92), never taller than the Intrasoft logo, 32px clear space.
- SAP's trademark statement word for word in the footer. "E-Book" spelling. "SAP Gold Partner".
- Colours: navy #132146, Intrasoft blue #00A7E3, light blue #78DCFF, red #CD0000 (accent only).
- Buttons name the actual E-Book / the actual offer.
"""
import re, json, sys, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_WHITE = 'https://files.leadconnectorhq.com/file/6af2d08730caaf80f6316eda/intrasoft-logo-white-official.png'
SAP_GP = 'https://files.leadconnectorhq.com/file/6af83e857c3b573a622e1a47/email-sap-gold-partner.png'
PARTNER_URL = 'https://www.sap.com/partners/profile/intrasoft-middle-east'
COVER_GF = 'https://files.leadconnectorhq.com/file/6af83e85893246071f7028c8/email-cover-gf.png'
COVER_BDC = 'https://files.leadconnectorhq.com/file/6af83e8677a01e4622d827bc/email-cover-bdc.png'
NAVY, BLUE, LIGHT, RED = '#132146', '#00A7E3', '#78DCFF', '#CD0000'
FONT = "Arial,Helvetica,sans-serif"
TM = ('SAP, the SAP logo, and the SAP partner logos are trademarks or registered trademarks of SAP SE or an SAP affiliated company in Germany and other countries.')

PRODUCTS = {
    'grow-fast': dict(md='grow-fast-nurture.md', label='SAP GROW Fast', eyebrow='SAP GROW FAST', bar=BLUE, cover=COVER_GF,
                      links={'[E-BOOK LINK]': '{{ custom_values.sap_grow_fast_ebook_url }}', '[FIT CHECK LINK]': '{{ custom_values.sap_grow_fast_fit_check_url }}'}),
    'bdc': dict(md='bdc-nurture.md', label='SAP BDC', eyebrow='SAP BUSINESS DATA CLOUD', bar=RED, cover=COVER_BDC,
                links={'[E-BOOK LINK]': '{{ custom_values.sap_bdc_ebook_url }}', '[E-BOOK 2 LINK]': '{{ custom_values.sap_bdc_ebook_2_url }}',
                       '[REVIEW LINK]': '{{ custom_values.sap_bdc_data_review_url }}'}),
    'bdc-ai': dict(md='bdc-ai-nurture.md', label='SAP BDC AI', eyebrow='SAP BUSINESS DATA CLOUD', bar=RED, cover=COVER_BDC,
                   links={'[E-BOOK LINK]': '{{ custom_values.sap_bdc_ebook_url }}', '[AI REVIEW LINK]': '{{ custom_values.sap_bdc_ai_review_url }}'}),
}
NAME = '{{ custom_values.sap_email_sender_name }}'
TITLE = '{{ custom_values.sap_email_sender_title }}'

def inline(t, links):
    t = html.escape(t, quote=False)
    for k, v in links.items(): t = t.replace(html.escape(k), v)
    t = t.replace('[SENDER NAME]', NAME).replace('[TITLE], Intrasoft Middle East', TITLE)
    t = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2" style="color:#0077B6;font-weight:700;text-decoration:underline">\1</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#132146">\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t

def button(text, url, primary=True):
    if primary:
        return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 24px"><tr><td style="border-radius:10px;background:{BLUE}">'
                f'<a href="{url}" style="display:block;padding:16px 24px;font-family:{FONT};font-size:16px;font-weight:700;line-height:1.35;color:{NAVY};text-decoration:none;text-align:center;border-radius:10px">{text}</a></td></tr></table>')
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin:6px 0 22px"><tr><td style="border-radius:10px;border:2px solid {NAVY}">'
            f'<a href="{url}" style="display:block;padding:12px 22px;font-family:{FONT};font-size:15px;font-weight:700;line-height:1.35;color:{NAVY};text-decoration:none;border-radius:8px">{text}</a></td></tr></table>')

def render_body(lines, links):
    out, para, lst, ltype = [], [], [], None
    def flush_p():
        nonlocal para
        if para:
            txt = '<br>'.join(inline(x, links) for x in para)
            if para[0].startswith('P.S.'):
                out.append(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 6px"><tr><td style="padding:14px 18px;background:#F1F7FC;border-left:4px solid {BLUE};border-radius:6px;font-family:{FONT};font-size:15px;line-height:1.6;color:#4A5878">{txt}</td></tr></table>')
            else:
                out.append(f'<p style="margin:0 0 18px;font-family:{FONT}">{txt}</p>')
            para = []
    def flush_l():
        nonlocal lst, ltype
        if lst:
            if ltype == 'ol':
                items = ''.join(f'<tr><td width="34" valign="top" style="padding:0 0 12px"><div style="width:24px;height:24px;border-radius:12px;background:{NAVY};color:#fff;font-family:{FONT};font-size:13px;font-weight:700;line-height:24px;text-align:center">{i+1}</div></td><td style="padding:0 0 12px;font-family:{FONT};font-size:16px;line-height:1.6">{inline(x, links)}</td></tr>' for i, x in enumerate(lst))
            else:
                items = ''.join(f'<tr><td width="34" valign="top" style="padding:0 0 12px"><div style="width:22px;height:22px;border-radius:11px;background:{BLUE};color:{NAVY};font-family:{FONT};font-size:13px;font-weight:700;line-height:22px;text-align:center">&#10003;</div></td><td style="padding:0 0 12px;font-family:{FONT};font-size:16px;line-height:1.6">{inline(x, links)}</td></tr>' for x in lst)
            out.append(f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 0 10px">{items}</table>')
            lst = []
    sig = []
    def flush_sig():
        nonlocal sig
        if not sig: return
        greet = [x for x in sig if x.rstrip().endswith(',')]
        name_title = [x for x in sig if not x.rstrip().endswith(',')]
        g = f'<div style="font-family:{FONT};font-size:16px;color:#4A5878;margin-bottom:6px">{inline(greet[0], links)}</div>' if greet else ''
        n = f'<div style="font-family:{FONT};font-size:16px;font-weight:700;color:{NAVY}">{NAME}</div><div style="font-family:{FONT};font-size:14px;color:#4A5878">{TITLE}</div>'
        out.append(f'<div style="margin:14px 0 8px">{g}{n}</div>')
        sig = []
    for ln in lines:
        s = ln.rstrip()
        if not s.strip():
            flush_p(); flush_l(); flush_sig(); continue
        if s.startswith(('Best regards,', 'Thank you for reading,')) or s.strip() in ('[SENDER NAME]', '[TITLE], Intrasoft Middle East'):
            flush_p(); flush_l(); sig.append(s); continue
        flush_sig()
        m = re.match(r'^\*\*\[(.+?)\]\((.+?)\)\*\*$', s)
        if m:
            flush_p(); flush_l()
            url = m.group(2)
            for k, v in links.items(): url = url.replace(k, v)
            out.append(button(inline(m.group(1), links), url)); continue
        m = re.match(r'^\[(.+?)\]\((.+?)\)$', s)
        if m:
            flush_p(); flush_l()
            url = m.group(2)
            for k, v in links.items(): url = url.replace(k, v)
            out.append(button(inline(m.group(1), links), url, primary=False)); continue
        m = re.match(r'^(-|\d+\.)\s+(.*)', s)
        if m:
            flush_p(); ltype = 'ol' if m.group(1)[0].isdigit() else 'ul'; lst.append(m.group(2)); continue
        flush_l(); para.append(s)
    flush_p(); flush_l(); flush_sig()
    # a lone "[SENDER NAME]" sign-off still gets the title line (handled in flush_sig)
    return '\n'.join(out)

def wrap(content, subject, preview, p, eid, cover, receiving):
    n = int(re.sub(r'\D', '', eid) or 0)
    tag = 'YOUR E-BOOK' if eid.startswith('E0') else f'{n} OF 5'
    eyebrow = f'{p["eyebrow"]} &nbsp;&middot;&nbsp; {tag}'
    h1 = html.escape(subject, quote=False)
    cover_td = (f'<td class="stk" width="150" valign="middle" align="right" style="padding-left:18px"><img src="{cover}" width="150" alt="E-Book cover" style="display:block;width:150px;max-width:100%;height:auto;border-radius:6px;border:0"></td>') if cover else ''
    text_w = '' if cover else ' colspan="1"'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light">
<title>{html.escape(subject, quote=False)}</title>
<style>
  @media only screen and (max-width:620px){{
    .px{{padding-left:22px !important;padding-right:22px !important}}
    .h1{{font-size:24px !important;line-height:1.25 !important}}
    .stk{{display:block !important;width:100% !important;padding:18px 0 0 0 !important;text-align:left !important}}
    .stk img{{width:140px !important}}
  }}
</style></head>
<body style="margin:0;padding:0;background:#EAF3FB">
<span style="display:none;max-height:0;overflow:hidden;opacity:0;mso-hide:all">{html.escape(preview)}</span>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EAF3FB"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:14px;overflow:hidden">
<tr><td style="height:5px;background:{p['bar']};font-size:0;line-height:0">&nbsp;</td></tr>
<tr><td class="px" style="background:{NAVY};padding:24px 32px 0"><img src="{LOGO_WHITE}" width="112" alt="Intrasoft Middle East" style="display:block;width:112px;height:auto;border:0"></td></tr>
<tr><td class="px" style="background:{NAVY};padding:28px 32px 34px">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
    <td{text_w} valign="middle" class="stk" style="font-family:{FONT}">
      <div style="font-size:12px;font-weight:700;letter-spacing:1.6px;color:{LIGHT};text-transform:uppercase">{eyebrow}</div>
      <div class="h1" style="margin-top:10px;font-size:28px;line-height:1.22;font-weight:700;color:#ffffff">{h1}</div>
    </td>{cover_td}
  </tr></table>
</td></tr>
<tr><td class="px" style="padding:34px 32px 20px;font-family:{FONT};font-size:16px;line-height:1.65;color:#1B2540">
{content}
</td></tr>
<tr><td class="px" style="background:{NAVY};padding:28px 32px 26px">
  <table role="presentation" cellpadding="0" cellspacing="0"><tr>
    <td valign="middle"><img src="{LOGO_WHITE}" width="120" alt="Intrasoft Middle East" style="display:block;width:120px;height:auto;border:0"></td>
    <td width="32" style="font-size:0;line-height:0">&nbsp;</td>
    <td valign="middle"><a href="{PARTNER_URL}"><img src="{SAP_GP}" width="96" alt="SAP Gold Partner" style="display:block;width:96px;height:auto;border:0"></a></td>
  </tr></table>
  <div style="margin-top:18px;font-family:{FONT};font-size:12px;line-height:1.6;color:#B9C8DE"><strong style="color:#ffffff">Intrasoft Middle East</strong> &middot; SAP Gold Partner<br>{receiving}</div>
  <div style="margin-top:12px;font-family:{FONT};font-size:11px;line-height:1.6;color:#9FB2CE">{TM}</div>
</td></tr>
</table></td></tr></table></body></html>'''

def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    result = []
    for key, p in PRODUCTS.items():
        md = open(os.path.join(HERE, p['md'])).read()
        for m in re.finditer(r'^## (E\d[a-z]?) · (.+?)\n(.*?)(?=^---\s*$)', md, re.S | re.M):
            eid, head, block = m.group(1), m.group(2).strip(), m.group(3)
            subj = re.search(r'^\*\*Subject:\*\*\s*(.+)$', block, re.M).group(1).strip()
            alt = re.search(r'^\*\*Alt subject:\*\*\s*(.+)$', block, re.M).group(1).strip()
            prev = re.search(r'^\*\*Preview:\*\*\s*(.+)$', block, re.M).group(1).strip()
            body = block[block.index(prev) + len(prev):].strip('\n').splitlines()
            content = render_body(body, p['links'])
            first = eid == 'E0' or eid == 'E0b'
            cover = p['cover'] if (first and eid != 'E0b') else ''
            receiving = ("You're receiving this because you downloaded an E-Book from Intrasoft." if first else
                         "You're receiving this because you downloaded the E-Book and chose to hear from Intrasoft. You can unsubscribe at any time.")
            h = wrap(content, subj, prev, p, eid, cover, receiving)
            leftover = re.sub(r'\{\{.*?\}\}', '', re.sub(r'<[^>]+>', '', h))
            assert not re.search(r'\[[A-Z0-9 ]+\]', leftover), (key, eid, re.findall(r'\[[A-Z0-9 ]+\]', leftover))
            title = f"{p['label']} · {eid} · {head}"
            fn = f'{key}-{eid}.html'
            open(os.path.join(out_dir, fn), 'w').write(h)
            result.append(dict(product=key, id=eid, title=title, subject=subj, alt_subject=alt, preview=prev, file=fn))
    json.dump(result, open(os.path.join(out_dir, 'index.json'), 'w'), indent=1, ensure_ascii=False)
    return result

if __name__ == '__main__':
    for r in build(sys.argv[1]): print(r['title'], '|', r['subject'])
