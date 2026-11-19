from components import *

GF_PDF = 'https://files.leadconnectorhq.com/file/6af2d089923b4bc1094f2a1b/sap-grow-fast-myth-busting-e-book.pdf'
COVER = 'https://assets.cdn.filesafe.space/vhJRhZJvL4LvDBJd7NM0/media/'
GF_BOOK = 'SAP GROW Fast Myth Busting E-Book'
GF_SEND = 'Send me the SAP GROW Fast Myth Busting E-Book'
GF_HEAD = 'Get the Myth Busting E-Book'
GF_MAIN = 'Get the SAP GROW Fast Myth Busting E-Book'
GF_OK = 'Your copy of the SAP GROW Fast Myth Busting E-Book is ready'
GF_TOC = [('The 10 most common myths', 'about SAP Cloud ERP, from cost and company size to speed, customization and ROI'),
          ('How a predefined scope', 'keeps ERP modernization under control'),
          ('What growing companies gain', 'by moving to cloud ERP'),
          ('How to decide', 'whether GROW Fast fits your business')]

MYTHS = [("SAP is too expensive for a company our size.", "The SAP subscription and Intrasoft's implementation service are priced separately, and the service price for the predefined scope is <b>set upfront</b>. You know the commitment before you decide."),
         ("ERP projects always run late and over budget.", "GROW Fast is built on a <b>predefined scope</b>, SAP best practices and a structured method, with scope and service price agreed before work begins."),
         ("ERP always takes a year or more.", "GROW Fast <b>targets go-live in about four months</b>, using SAP's preconfigured processes as the starting point."),
         ("Every process must be customized before go-live.", "SAP best practices give you <b>a proven starting point</b>, so you begin with standard processes instead of designing everything from scratch."),
         ("Enterprise ERP needs a large in-house SAP team.", "<b>SAP runs the cloud system.</b> Intrasoft provides the implementation, user training and ongoing support."),
         ("We need to be bigger before ERP makes sense.", "Waiting until systems become unmanageable makes the move harder. GROW Fast is <b>designed for growing mid-size companies</b>.")]

FAQ = [("What is SAP GROW Fast?", "An accelerated way to start with SAP Cloud ERP (public edition). It uses SAP's preconfigured best practices and a <b>predefined implementation scope</b>, delivered by an SAP partner such as Intrasoft."),
       ("How is the price structured?", "Two parts: the SAP Cloud ERP subscription and Intrasoft's fixed-price GROW Fast service for the predefined scope. <b>Both are agreed upfront.</b> Extra scope, integrations or change requests are quoted separately."),
       ("How long does implementation take?", "The target is <b>about four months to go-live</b>. The actual timeline depends on scope, data readiness and your team's availability."),
       ("Our data isn't ready. Can we still start?", "Yes. Data preparation is part of the plan. <b>Responsibilities are agreed upfront</b>, and readiness is checked before go-live."),
       ("Who runs the system after go-live?", "<b>SAP runs the cloud system</b>, including infrastructure, updates, security and maintenance. Intrasoft provides user training and ongoing support."),
       ("Is this right for us?", "GROW Fast suits <b>growing mid-size companies, especially manufacturers</b>, that have outgrown spreadsheets, disconnected systems or a legacy ERP. It's less suited to companies needing extensive bespoke development.")]

WHY = [('layers', 'Structured implementation', 'A predefined scope and SAP best-practice method, with clear milestones.'),
       ('people', 'User training', 'Your team learns to run finance, supply chain and HR in SAP Cloud ERP.'),
       ('chat', 'Regional presence', '26 years in the region, with Arabic and English-speaking teams.'),
       ('cog', 'Ongoing support', 'Support continues after go-live, including help adding capabilities.')]

def myth_rows():
    return [(f'“{m}”', f'<b>Reality:</b> {r}') for m, r in MYTHS]

def steps_dark():
    s = [('Align on priorities', 'Confirm priorities, roles and timeline within the predefined scope.'), ('Configure', "Set up the agreed solution with SAP's preconfigured processes."),
         ('Validate and prepare', 'Test, prepare data and train users before go-live.'), ('Launch', 'Go live with the agreed scope and support users as they start.'),
         ('Support and expand', 'Ongoing support, and help adding capabilities as you grow.')]
    st = ''.join(f'<div class="isl-step isl-rv"><i>{i+1}</i><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(s))
    return (f'<div class="isl-steps">{st}</div><div class="isl-time isl-rv"><div class="isl-time-top"><strong>Target: about 4 months to go-live</strong><span>Depends on scope, data readiness and agreed project conditions.</span></div>'
            '<div class="isl-bar"><i></i></div><div class="isl-months"><span>Month 1</span><span>Month 2</span><span>Month 3</span><span>Month 4</span></div></div>'
            f'<p class="isl-price-note isl-rv">{ico("card")}<span><b>Upfront, transparent implementation pricing.</b> A fixed fee for Intrasoft\'s agreed, predefined scope, separate from the SAP subscription. Extra scope, integrations or change requests are quoted separately.</span></p>')

# ---------------------------------------------------------------- V2: decisions (light hero)
def gf_v2():
    cfg = cfg_block('grow-fast-v2-answers', GF_PDF, COVER + 'e1457bb8-e1de-4e03-a320-27210bbd34bb.webp', '/gf-thank-you')
    board = ('<div class="isl-board"><p class="isl-board-h">Before the first workshop</p><h3>Decisions to make early</h3><ul>'
             '<li><i>1</i><b>Priorities</b><span>Which processes matter most at go-live?</span><em>✓</em></li>'
             '<li><i>2</i><b>Scope</b><span>What\'s in, and what waits for phase two?</span><em>✓</em></li>'
             '<li><i>3</i><b>Changes</b><span>How are new requests handled once work starts?</span><em>✓</em></li></ul>'
             '<div class="isl-board-foot">In SAP GROW Fast, these are agreed upfront, before the work begins.</div></div>')
    hero = ('<section class="isl-hero isl-light"><div class="isl-wrap isl-hero-grid"><div>'
            + eyebrow('Free E-Book · For CEOs, CFOs and CIOs in Saudi Arabia') +
            f'<h1>Your next ERP decision starts with {g("clearer answers.")}</h1>'
            '<p class="isl-tagline">Understand the questions that matter before moving to cloud ERP.</p>'
            '<p class="isl-lead">What is your current ERP really costing you in maintenance, manual work and disconnected reporting? Before you commit to anything, get clear answers on SAP Cloud ERP with SAP GROW Fast.</p>'
            f'<div class="isl-hero-ctas">{btn(GF_MAIN + " " + ico("down"), cta="hero")}{btn("See what to weigh up", "#isl-cost", "hero-2", ghost=True)}</div>'
            f'<div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>{lockup(light=True)}</div>'
            f'<div class="isl-visual" aria-hidden="true">{board}</div></div></section>')
    ledger_rows = [('Maintenance', 'of the old system or tools'), ('Manual work', 'hours of reconciliation every month'), ('Waiting', 'decisions held up by reports that arrive late')]
    rows = ''.join(f'<div class="isl-led-row"><div><b>{b}</b><span class="isl-led-d">{d}</span></div><div class="isl-led-ctl"><span class="isl-led-state">Tick if you do</span><button type="button" class="isl-switch" role="switch" aria-checked="false" aria-label="We pay for {b.lower()}"><i></i></button></div></div>' for b, d in ledger_rows)
    msgs = ['Tick the costs you recognise. Most companies have never added them up.',
            '<b>1 of 3.</b> It is the one you already pay, before any new spend. Worth putting next to the cost of the alternative.',
            '<b>2 of 3.</b> These costs repeat every month. A side-by-side view with GROW Fast is the next step.',
            '<b>All 3.</b> Before comparing anything, list what your current setup costs you. The E-Book starts with the cost myth.']
    s_cost = section(head('Start with what you already pay', f'What is your current setup {g("really costing you?")}', 'The cost people forget is the one they already pay. Tick what applies to your company.')
                     + f'<div class="isl-ledger isl-rv" data-ledger="{jattr(msgs)}">{rows}<div class="isl-led-sum"><p>{msgs[0]}</p>{btn("Read the facts in the E-Book", cta="ledger")}</div></div>', 'isl-pad isl-soft', 'isl-cost')
    eq = ('<div class="isl-eq isl-rv"><div><small>Part 1</small><b>The SAP Cloud ERP subscription</b><p>What you pay SAP for the cloud system.</p></div><div class="isl-eq-op">+</div>'
          '<div><small>Part 2</small><b>Intrasoft\'s implementation service</b><p>A predefined scope, with the service price agreed upfront.</p></div><div class="isl-eq-op">=</div>'
          '<div class="isl-eq-res"><small>The result</small><b>A commitment you understand before you start</b><p>Extra scope, integrations or change requests are quoted separately.</p></div></div>')
    s_eq = section(head('Two numbers, not one', f'The cost has {g("two clear parts")}', 'With SAP GROW Fast, you can see both before you decide.') + eq)
    tabs_html = tabs([
        ('Priorities', '<h3>Which processes matter most at go-live?</h3><p>You confirm your <b>priorities, roles and timeline</b> within the predefined scope, before the work begins.</p>'),
        ('Scope', '<h3>What\'s in, and what waits for phase two?</h3><p>You start from a <b>predefined scope</b>: core finance, supply chain and HR, built on SAP best practices. No open-ended project, no scope creep.</p>'),
        ('Changes', '<h3>How are new requests handled once work starts?</h3><p>Extra scope, integrations or change requests are <b>quoted separately</b>, so you know what you\'re committing to before you start.</p>')])
    s_tabs = section(head('Why ERP projects run over', f'Make the important decisions {g("early")}', "When projects overrun, the software is rarely the cause. It's usually the decisions nobody made early.") + tabs_html, 'isl-pad isl-dark')
    s_myths = section(head('Myth busting', f'What\'s actually changed with {g("SAP Cloud ERP")}', 'Tap a myth to see the reality. The E-Book covers ten of them in depth.') + faq_acc(myth_rows())
                      + f'<div class="isl-proof isl-rv"><div class="isl-proof-n"><b>15</b><small>weeks</small></div><p>One of the SAP customer results in the E-Book: <b>PureTech Scientific deployed SAP Cloud ERP in just 15 weeks, with no internal IT team.</b></p></div>', 'isl-pad isl-soft')
    cols = ('<div class="isl-cols isl-rv">'
            '<div class="isl-col"><small>CEO</small><h3>Scale without losing control</h3><p>An integrated foundation that supports growth and shows the whole business more clearly.</p></div>'
            '<div class="isl-col"><small>CFO</small><h3>Know the commitment upfront</h3><p>Transparent implementation pricing, clear scope boundaries and more timely financial information.</p></div>'
            '<div class="isl-col"><small>CIO</small><h3>A manageable cloud foundation</h3><p>A structured method, proven SAP processes, defined responsibilities and support beyond go-live.</p></div></div>')
    s_leaders = section(head('For every decision-maker', f'The questions {g("each leader")} asks', None) + cols)
    vt = ''.join(f'<div class="isl-vs isl-rv"><i>{i+1}</i><div><b>{t}</b><p>{p}</p></div></div>' for i, (t, p) in enumerate([
        ('Align on priorities', 'Confirm your priorities, roles and timeline within the predefined scope.'), ('Configure to proven practices', 'Use SAP preconfigured processes and relevant templates to set up the agreed solution.'),
        ('Validate and prepare', 'Test the solution, prepare data, train users and check readiness for go-live.'), ('Launch and enable', 'Go live with the agreed scope and support users as they start working in the system.'),
        ('Support and expand', 'Ongoing support, and help assessing additional capabilities as the business grows.')]))
    s_path = section(head('How GROW Fast works', f'A structured path to {g("SAP Cloud ERP")}', 'Target: about 4 months to go-live. The timeline depends on scope, data readiness and agreed project conditions.') + f'<div class="isl-vt">{vt}</div>', 'isl-pad isl-soft isl-light-t')
    conv = convert('center', book=GF_BOOK, cover_html=cover('isl-cv', 'SAP GROW Fast Myth Busting E-Book cover'), toc=GF_TOC, eyebrow_t='Free E-Book',
                   send=GF_SEND, sub='Tell us where to send it. It opens straight away, and a copy goes to your inbox.', ok_title=GF_OK,
                   h2='Get clear answers, free.', lead='The SAP GROW Fast Myth Busting E-Book covers the ten most common myths about SAP Cloud ERP, so leadership can align before the first workshop.',
                   chips=['10 myths, answered', 'Cost and company size', 'Speed and customization', 'Does GROW Fast fit?'])
    s_why = section(why_band('Why Intrasoft', f'One partner from first workshop {g("to life after go-live")}', 'Intrasoft is an SAP Gold Partner that delivers SAP GROW Fast from start to finish, and stays with you afterwards.', WHY))
    s_faq = section(head('FAQ', 'Questions leaders ask us') + faq_acc(FAQ), 'isl-pad isl-soft')
    body = '\n'.join([topbar('<b>Free E-Book:</b> clear answers on SAP Cloud ERP for CEOs, CFOs and CIOs.'), header(GF_HEAD), hero, trust(), s_cost, s_eq, s_tabs, s_myths, s_path, s_leaders, conv, s_why, s_faq,
                     final(f'Make the important decisions {g("early.")}', 'The SAP GROW Fast Myth Busting E-Book. Free, with instant access.', GF_MAIN), footer(), sticky(GF_HEAD)])
    return page('Clearer Answers on Cloud ERP | Intrasoft', 'Your next ERP decision starts with clearer answers. Download the free SAP GROW Fast Myth Busting E-Book from Intrasoft, an SAP Gold Partner.', cfg, body), GF_SEND

# ---------------------------------------------------------------- V3: growth (dark hero + chart)
def gf_v3():
    cfg = cfg_block('grow-fast-v3-growth', GF_PDF, COVER + '9665f7b7-e17c-4454-89d9-2fb8baffe9a8.webp', '/gf-thank-you')
    chart = ('<div class="isl-chart" aria-hidden="true"><svg viewBox="0 0 520 320"><defs><linearGradient id="isl-gapg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF6B6B" stop-opacity=".35"/><stop offset="1" stop-color="#FF6B6B" stop-opacity=".05"/></linearGradient></defs>'
             '<path d="M40 20V280H500" fill="none" stroke="#46608A" stroke-width="2"/>'
             '<path d="M40 220H500M40 160H500M40 100H500" stroke="#2A3F6E" stroke-width="1" stroke-dasharray="4 6"/>'
             '<path d="M40 250C180 240 300 200 480 60L480 235C380 240 220 248 40 250Z" fill="url(#isl-gapg)"/>'
             '<path class="isl-gl2" d="M40 250C220 248 380 240 480 235" fill="none" stroke="#FF6B6B" stroke-width="5" stroke-linecap="round" stroke-dasharray="900"/>'
             '<path class="isl-gl" d="M40 250C180 240 300 200 480 60" fill="none" stroke="#00A7E3" stroke-width="6" stroke-linecap="round"/>'
             '<circle cx="480" cy="60" r="8" fill="#78DCFF"/><text x="388" y="190" fill="#fff" font-size="17" font-weight="800" font-family="Inter,sans-serif">The gap</text>'
             '<text x="40" y="306" fill="#8EA3C0" font-size="13" font-family="Inter,sans-serif">Time</text></svg>'
             '<div class="isl-chart-key"><span><i></i>Your business</span><span><i class="r"></i>Your systems</span></div><small>Illustration, not real data.</small></div>')
    hero = ('<section class="isl-hero"><div class="isl-wrap isl-hero-grid"><div>' + eyebrow('Free E-Book · For growing manufacturers in Saudi Arabia') +
            f'<h1>Is your business growing {g("faster than your systems?")}</h1>'
            '<p class="isl-tagline">Connect finance, operations and supply chain with SAP Cloud ERP.</p>'
            '<p class="isl-lead">When growth outpaces spreadsheets and legacy ERP, every report takes longer and every decision waits. The free SAP GROW Fast Myth Busting E-Book shows why growing companies are revisiting SAP Cloud ERP now.</p>'
            f'<div class="isl-hero-ctas">{btn(GF_MAIN + " " + ico("down"), cta="hero")}{btn("See the month-end test", "#isl-flow", "hero-2", ghost=True)}</div>'
            f'<div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>{lockup()}</div>'
            f'<div class="isl-visual">{chart}</div></div></section>')
    nodes = [('doc', 'Procurement', 'One file', 'Same data'), ('grid', 'Inventory', 'Another file', 'Same data'), ('truck', 'Supply chain', 'Another system', 'Same data'), ('card', 'Finance', 'A third file', 'Same data'), ('chart', 'Leadership', 'Waits for the report', 'Sees it as it happens')]
    nd = ''.join(f'<div class="isl-node"><span class="isl-man">Manual</span><i>{ico(ic)}</i><b>{t}</b><small><span class="isl-t-off">{a}</span><span class="isl-t-on">{b}</span></small></div>' for ic, t, a, b in nodes)
    flow = (f'<div class="isl-flowbox isl-rv" data-switch><div class="isl-switch-row"><span class="isl-s-off">Separate files</span><button type="button" class="isl-switch" role="switch" aria-checked="false" aria-label="Show the month-end with one system"><i></i></button><span class="isl-s-on">One system</span></div>'
            f'<div class="isl-flow">{nd}</div><p class="isl-flow-msg" data-off="Someone spends days matching them before leadership sees a single report." data-on="With finance, procurement, inventory and HR in one system, the data flows between processes as the work happens. The effort goes into reading the numbers, not assembling them.">Someone spends days matching them before leadership sees a single report.</p></div>'
            '<p class="isl-fine">An illustration, not a specific client. Flip the switch to compare.</p>')
    s_flow = section(head('The month-end test', f'One month-end, {g("two ways")}', 'Procurement has one file, inventory another and finance a third. You may recognize it.') + flow
                     + f'<div class="isl-callout isl-rv">{ico("factory")}<div><p><b>Relevant for manufacturers.</b> The scope is defined up front: core finance, supply chain and HR, built on SAP best practices. No open-ended project, no scope creep.</p><div class="isl-chips-row" style="margin-top:10px"><span style="background:#E8F6FD;color:#132146">Finance</span><span style="background:#E8F6FD;color:#132146">Procurement</span><span style="background:#E8F6FD;color:#132146">Inventory</span><span style="background:#E8F6FD;color:#132146">Supply chain</span><span style="background:#E8F6FD;color:#132146">HR</span></div></div></div>', 'isl-pad', 'isl-flow')
    radios = [('sheets', 'sheet', 'Spreadsheets', 'Most of our numbers live in files', 'The more you grow on spreadsheets, the more data and processes there are to move later. The E-Book shows what moving to cloud ERP looks like <b>today</b>.'),
              ('separate', 'link', 'Separate systems', 'Several tools that do not talk to each other', 'Disconnected systems mean manual reporting every quarter. SAP Cloud ERP brings <b>core finance, supply chain and HR</b> onto one cloud platform.'),
              ('legacy', 'wrench', 'A legacy ERP', 'Workarounds make every change slower', 'Older ERP, point integrations and spreadsheet workarounds make every change <b>slower and riskier</b>. See what has changed about cost, time and effort.')]
    rd = ''.join(f'<button type="button" class="isl-radio" role="radio" aria-checked="false" data-k="{k}" data-msg="{esc(m)}"><span class="isl-ic">{ico(ic)}</span><b>{t}</b><span>{d}</span></button>' for k, ic, t, d, m in radios)
    s_rad = section(head('Where are you today?', f'Pick the one that {g("sounds like you")}', None) + f'<div data-radios class="isl-rv"><div class="isl-radios" role="radiogroup" aria-label="Where are you today">{rd}</div><div class="isl-radio-out" style="display:none"><p></p>{btn(GF_MAIN, cta="stage")}</div></div>', 'isl-pad isl-soft')
    snaps = ''.join(f'<div class="isl-snapc"><span class="isl-tag">Myth {i+1}</span><q>{m}</q><div class="isl-real"><small>The reality</small>{r}</div></div>' for i, (m, r) in enumerate(MYTHS))
    s_myth = section(head('Myth busting', f'Six things people still believe {g("about SAP")}', 'Swipe through. The E-Book covers ten of them in depth.') + f'<div class="isl-snap isl-rv">{snaps}</div><p class="isl-snap-hint">Swipe or scroll sideways</p>'
                     + f'<div class="isl-proof isl-rv"><div class="isl-proof-n"><b>15</b><small>weeks</small></div><p>One of the SAP customer results in the E-Book: <b>PureTech Scientific deployed SAP Cloud ERP in just 15 weeks, with no internal IT team.</b></p></div>')
    s_steps = section(head('How GROW Fast works', f'A structured path, {g("step by step")}', None) + steps_dark(), 'isl-pad isl-dark')
    lead = tabs([('CEO', '<h3>Scale without losing control</h3><p>An integrated foundation that supports growth and helps you see the whole business more clearly.</p>'),
                 ('CFO', '<h3>Know the commitment upfront</h3><p>Transparent implementation pricing, clear scope boundaries and more timely access to financial information.</p>'),
                 ('CIO', '<h3>A manageable cloud ERP foundation</h3><p>A structured method, proven SAP processes, defined responsibilities and partner support beyond go-live.</p>')])
    s_lead = section(head('For every decision-maker', f'What it means for {g("your leadership team")}', None) + lead, 'isl-pad isl-soft')
    conv = convert('split', book=GF_BOOK, cover_html=cover('isl-bigcover', 'SAP GROW Fast Myth Busting E-Book cover'), toc=GF_TOC, eyebrow_t='Free E-Book', h2='Decide on facts, not assumptions.',
                   send=GF_SEND, sub='Tell us where to send it. It opens straight away, and a copy goes to your inbox.', ok_title=GF_OK)
    s_why = section(head('Why Intrasoft', f'One partner from first workshop {g("to life after go-live")}') + why_grid([(t, p) for _, t, p in WHY]) + f'<div class="isl-why-lock isl-rv">{lockup(light=True)}</div>', 'isl-pad isl-soft')
    s_faq = section(head('FAQ', 'Questions leaders ask us') + faq_acc(FAQ, one=True))
    body = '\n'.join([topbar('<b>Free E-Book:</b> is your business growing faster than your systems?'), header(GF_HEAD), hero, trust(), s_flow, s_rad, s_myth, s_steps, s_lead, conv, s_why, s_faq,
                     final(f'Don\'t let old assumptions {g("slow your growth.")}', 'The SAP GROW Fast Myth Busting E-Book. Free, with instant access.', GF_MAIN), footer(), sticky(GF_HEAD)])
    return page('Growing Faster Than Your Systems? | Intrasoft', 'Is your business growing faster than your systems? Download the free SAP GROW Fast Myth Busting E-Book from Intrasoft, an SAP Gold Partner.', cfg, body), GF_SEND
