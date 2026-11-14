from components import *

BDC_PDF = 'https://files.leadconnectorhq.com/file/6af2d08afbdd54a8278a436e/connect-and-harmonize-business-data-e-book.pdf'
V4_PDF = 'https://files.leadconnectorhq.com/file/6af2d463ddcd97ce5a9edc8a/driving-impactful-business-decisions-e-book.pdf'
COVER = 'https://assets.cdn.filesafe.space/vhJRhZJvL4LvDBJd7NM0/media/'
PRISM, SPHERE = COVER + 'dc63e9ca-1cbd-4e2e-98c1-e00b9ecd7c3a.webp', COVER + '9cbb60ab-2035-4968-b0d9-71b298831caa.webp'
BDC_BOOK = 'Connect and Harmonize Business Data to Amplify the Power of AI'
BDC_SEND = 'Send me the E-Book: ' + BDC_BOOK
BDC_HEAD = 'Get the Connect and Harmonize E-Book'
BDC_MAIN = 'Read the E-Book: ' + BDC_BOOK
BDC_OK = 'Your copy of ' + BDC_BOOK + ' is ready'
BDC_TOC = [('Why poor data quality and hard-to-harmonize data', 'stall data and AI innovation'),
           ('How SAP Business Data Cloud unifies SAP data', 'and connects third-party data, with full business context'),
           ('Where SAP Datasphere, SAP Analytics Cloud, SAP Business Warehouse and SAP Databricks', 'fit'),
           ('How AI-powered applications', 'turn that data into decisions across finance, supply chain and HR')]
SUB = 'Tell us where to send it. It opens straight away, and a copy goes to your inbox.'
AFTER_DL = ('What happens after I download the E-Book?', "You'll get the E-Book straight away. If you opted in, we'll follow up with a few relevant insights and an invitation to talk to a specialist, with no obligation.")
DATA_USE = ('How is my data used?', 'We use your details to deliver the resource and, only if you opted in, to send related communications. See our privacy notice for details.')
WHY = [('shield', 'SAP Gold Partner', 'We work within the SAP ecosystem and follow SAP-approved delivery practices.'),
       ('target', 'Business-first approach', 'We start with the decisions your teams need to make, then shape the data and analytics to support them.'),
       ('people', 'Enablement and support', 'We train your teams and keep supporting them after go-live, so the solution keeps delivering value.')]
FIN_FAQ = [('Is SAP Analytics Cloud only for reporting and dashboards?', 'No. SAP Analytics Cloud supports analytics and planning, including financial planning, scenario modeling and forecasting. The capabilities you use depend on your requirements and the solution design.'),
           ('We already plan in Excel. Why consider SAC?', 'Excel remains a useful finance tool. But as models grow more complex and the need for collaboration, scenario comparison and changing assumptions increases, spreadsheet-heavy processes get harder to maintain. The aim is to find where your current approach creates limits, and whether SAC addresses them.'),
           ('Will our finance team need technical expertise?', "That depends on how the solution is designed and each user's tasks. Practical, role-based enablement is part of the delivery approach."),
           ('Can SAP Analytics Cloud work with our existing systems?', 'SAP Analytics Cloud offers integration capabilities. The right approach depends on your applications, data sources and architecture, and is reviewed during assessment and design.'),
           ('How long does implementation take?', 'It depends on scope: planning-model complexity, integrations, processes, testing and user readiness. We agree a realistic delivery plan with your stakeholders.'),
           ('What happens after go-live?', 'Planning requirements keep evolving. The offer includes options for ongoing managed services, support and optimization, subject to the agreed engagement scope.'), AFTER_DL]

def stat_band(src_note=True):
    s = ('<div class="isl-stats isl-rv"><div class="isl-stat"><b>55%</b><p>of 1,200 business and technology leaders cite poor data quality as their biggest challenge.</p></div>'
         '<div class="isl-stat"><b>Nearly half</b><p>point to the difficulty of harmonizing data across ecosystems as a key reason innovation stalls.</p></div></div>')
    return s + '<p class="isl-source">From a global survey cited in the E-Book.</p>' if src_note else s

def bars(hs, h2=None):
    return '<div class="isl-bars">' + ''.join(f'<i style="--h:{h}%;--h2:{(h2 or h)}%"></i>' for h in hs) + '</div>'

# ------------------------------------------------------------ V1: one truth (light hero)
def bdc_v1():
    cfg = cfg_block('bdc-v1-one-truth', BDC_PDF, PRISM, '/bdc-thank-you')
    reps = ('<div class="isl-reports" id="isl-reps"><div class="isl-reports-row">'
            f'<div class="isl-rep"><small>Finance report</small><b>Revenue last quarter</b>{bars([80, 45, 62], 70)}<em></em></div>'
            f'<div class="isl-rep"><small>Sales report</small><b>Revenue last quarter</b>{bars([50, 85, 35], 70)}<em></em></div>'
            f'<div class="isl-rep"><small>Operations report</small><b>Revenue last quarter</b>{bars([30, 55, 90], 70)}<em></em></div></div>'
            '<p class="isl-reports-msg" data-msg data-off="Three reports. Three different numbers." data-on="Same definitions. Same numbers.">Three reports. Three different numbers.</p>'
            '<div class="isl-reports-cta"><button type="button" class="isl-btn isl-btn-primary" data-demo="#isl-reps" data-label-off="See it with shared definitions" data-label-on="Show the problem again">See it with shared definitions</button></div></div>')
    hero = ('<section class="isl-hero isl-light"><div class="isl-wrap isl-hero-grid"><div>' + eyebrow('Free E-Book · For finance and business leaders in Saudi Arabia') +
            f'<h1>One business. {g("Too many versions of the truth?")}</h1><p class="isl-tagline">Same business. Same question. Different numbers.</p>'
            '<p class="isl-lead">When reports disagree, finding the reason becomes part of the job. This free SAP E-Book shows how SAP Business Data Cloud brings SAP and non-SAP data together with its business context, so teams work from the same definitions.</p>'
            f'<div class="isl-hero-ctas">{btn(BDC_MAIN + " " + ico("down"), cta="hero")}</div><div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>{lockup(light=True)}</div>'
            f'<div class="isl-visual">{reps}</div></div></section>')
    tb = tabs([('Definitions', '<h3>Are teams measuring the same thing?</h3><p>Before or after returns? Which entities? When definitions differ, <b>every number can be right and still disagree</b>.</p>'),
               ('Timing', '<h3>Do the reports cover the same period?</h3><p>Reports built on different cut-off dates will not match, even when the data underneath is identical.</p>'),
               ('Sources', '<h3>Which systems feed each report?</h3><p>When SAP and non-SAP systems feed different reports, each one carries <b>its own copy of the truth</b>.</p>')])
    tryit = ('<div class="isl-try isl-rv"><div><i>1</i><b>Pick one KPI</b>Revenue, margin, days sales outstanding. Anything leadership asks about often.</div><div><i>2</i><b>Ask two teams</b>Ask how each one calculates it.</div><div><i>3</i><b>Compare the answers</b>If they differ, the E-Book shows where to start.</div></div>')
    s_why_diff = section(head('The pattern', f'Why the numbers {g("differ")}', 'Nobody is wrong. The mismatch usually starts in one of three places.') + tb
                         + f'<div class="isl-callout isl-rv">{ico("warn")}<div><p><b>When that happens, meetings start with reconciling numbers instead of making decisions.</b></p></div></div>' + tryit)
    s_stats = section(head('The scale of the problem', f'It is not a lack of data. {g("It is a lack of trust.")}', None) + stat_band(), 'isl-pad isl-soft')
    ba = ('<div class="isl-ba"><div class="isl-ba-col isl-rv"><small>Without shared context</small><h3>Every report has its own version</h3><ul><li>Different definitions in every report</li><li>Data copied and stripped of its business meaning</li><li>Hours spent reconciling instead of deciding</li></ul></div>'
          '<div class="isl-ba-col isl-after isl-rv"><small>With SAP Business Data Cloud</small><h3>One business context</h3><ul><li>SAP and third-party data brought together</li><li>Curated data products keep their original business meaning</li><li>Every report starts from the same numbers</li></ul></div></div>')
    s_ba = section(head('How it works', f'Give your data {g("a shared business context")}', 'SAP Business Data Cloud harmonizes SAP and third-party data with its business context, so finance and operations work from the same definitions.') + ba)
    items = [('Budgets go out of date fast', 'Business conditions change, but the planning process struggles to keep pace.'), ('Time spent maintaining spreadsheets', 'Hours go into collecting, reconciling and updating numbers instead of exploring alternatives.'),
             ('"What if" takes too long', 'A simple scenario question turns into another lengthy planning exercise.'), ('Disconnected assumptions', "It's hard to see how a change in one business driver affects the wider financial picture."),
             ('Looking back, not ahead', 'Finance is busy explaining past performance when leadership needs forward-looking answers.')]
    rm = ['Tick the ones that sound like your planning process.', 'One is a common starting point.', 'Two is worth a closer look.', 'Three suggests the process, not the people, is the limit.', 'Four: the numbers exist, but the planning process gets in the way.', 'All five: the real problem is not a lack of data. It is the gap between the information you have and the decisions your business needs to make.']
    its = ''.join(f'<button type="button" class="isl-rc-item" aria-pressed="false"><i>✓</i><div>{t}<span>{d}</span></div></button>' for t, d in items)
    ring = (f'<div class="isl-ringbox isl-rv" data-ring="{jattr(rm)}"><div class="isl-ringwrap"><svg viewBox="0 0 210 210"><circle class="isl-ring-bg" cx="105" cy="105" r="90"/><circle class="isl-ring-fg" cx="105" cy="105" r="90"/></svg><div class="isl-ring-c"><div><b>0</b><br><small>of 5</small></div></div></div>'
            f'<div>{its}<p class="isl-rc-msg">{rm[0]}</p></div></div>')
    s_ring = section(head('Sound familiar?', f'The numbers exist. {g("The planning process gets in the way.")}', 'Tick the ones that apply to your finance team.') + ring, 'isl-pad isl-soft')
    persona = ('<div class="isl-persona isl-rv"><div><small>CFO or Finance Director</small><b>See potential outcomes before you decide</b><p>You want finance to contribute to strategic discussions, not only report historical results.</p></div>'
               '<div><small>Head of FP&amp;A</small><b>More capacity for analysis</b><p>Your team spends too long maintaining forecasts, reconciling spreadsheets and reacting to changing assumptions.</p></div>'
               '<div><small>Finance transformation lead</small><b>Technology people actually use</b><p>You want implementation, processes, training and ongoing improvement to work together.</p></div>'
               '<div><small>Rethinking your approach</small><b>Beyond the annual budget</b><p>You want to explore rolling forecasts, driver-based planning, scenario modeling or more connected planning workflows.</p></div></div>'
               '<p class="isl-notfor isl-rv"><b>This may not be the right fit if…</b> you only need a one-off dashboard, a simple report or a standalone technical deployment with no real financial planning requirement.</p>')
    s_pers = section(head('Who this is for', f'Built for finance leaders who need {g("more than another dashboard")}', None) + persona)
    vt = ''.join(f'<div class="isl-vs isl-rv"><i>{i+1}</i><div><b>{t}</b><p>{p}</p></div></div>' for i, (t, p) in enumerate([
        ('Assess and align', 'Agree priorities, scope and measures of success before implementation begins.'), ('Design the planning model', 'Define drivers, forecasting needs, scenarios, workflows and reporting.'),
        ('Implement with SAP Activate', 'Configure, test, validate and deploy the agreed SAP Analytics Cloud solution.'), ('Enable finance teams', 'Role-based training, participation and adoption planning.'), ('Optimize and evolve', 'Review usage, feedback and new requirements through agreed ongoing services.')]))
    s_path = section(head('Why Intrasoft is different', f'One connected journey, {g("from planning design to ongoing improvement")}', "Go-live doesn't automatically change how finance plans. Processes need designing, users need involving and the solution needs to evolve with the business.") + f'<div class="isl-vt">{vt}</div>', 'isl-pad isl-dark')
    mini = ('<div class="isl-mini isl-rv"><div><b>Planning and solution design</b><p>Start with the decisions your business needs to make.</p></div><div><b>SAP Analytics Cloud implementation</b><p>Turn your planning requirements into a practical, tested solution.</p></div>'
            '<div><b>Finance team enablement</b><p>A planning solution creates value when people can put it to work.</p></div><div><b>Managed services</b><p>Your planning requirements will not stand still. Neither should your solution.</p></div></div>')
    s_mini = section(head('What you get', f'One integrated partner. {g("A more connected planning capability.")}', 'Intrasoft brings planning design, SAP Analytics Cloud implementation, enablement and ongoing improvement together, as part of SAP Business Data Cloud.') + mini, 'isl-pad isl-soft')
    conv = convert('center', book=BDC_BOOK, cover_html=cover('isl-cv', BDC_BOOK + ' E-Book cover'), toc=BDC_TOC, eyebrow_t='Free E-Book', send=BDC_SEND, sub=SUB, ok_title=BDC_OK,
                   h2='Give your data a shared business context.', lead='The next business decision will not wait for your next annual budget. Reliable planning and scenario analysis start with connected, trusted business data.',
                   chips=['Why data stalls innovation', 'Shared business context', 'SAP Datasphere and SAC', 'From data to decisions'])
    s_why = section(why_band('Why Intrasoft', f'Your SAP partner for {g("data and analytics")}', 'Intrasoft helps organizations turn SAP data and analytics into value, from first conversation to ongoing support.', WHY))
    s_faq = section(head('FAQ', 'Common questions') + faq_acc(FIN_FAQ), 'isl-pad isl-soft')
    body = '\n'.join([topbar('<b>Free E-Book:</b> one business, one version of the truth.'), header(BDC_HEAD), hero, trust(), s_why_diff, s_stats, s_ba, s_ring, s_pers, s_path, s_mini, conv, s_why, s_faq,
                     final(f'Give your data {g("a shared business context.")}', 'Download the free SAP E-Book: ' + BDC_BOOK + '.', BDC_MAIN), footer(), sticky(BDC_HEAD)])
    return page('One Business, One Version of the Truth | Intrasoft', 'One business. Too many versions of the truth? Download the free SAP E-Book on connecting and harmonizing business data, from Intrasoft.', cfg, body), BDC_SEND

# ------------------------------------------------------------ V2: reliable AI (dark hero, CIO)
def bdc_v2():
    cfg = cfg_block('bdc-v2-reliable-ai', BDC_PDF, SPHERE, '/bdc-thank-you?for=ai')
    stack = ('<div class="isl-stack" aria-hidden="true"><div class="isl-layer isl-top-l"><small>Decisions</small><b>Analytics, planning and AI</b><p>Insight and action on data you can trust.</p><div class="isl-chips-row"><span>Joule</span><span>SAP Analytics Cloud</span><span>SAP Databricks</span></div></div>'
             '<div class="isl-flowdot"></div><div class="isl-layer"><small>Foundation</small><b>Governed, harmonized data</b><p>Business context kept. Quality and access under control.</p></div>'
             '<div class="isl-flowdot"></div><div class="isl-layer"><small>Sources</small><b>SAP and third-party data</b><p>Applications, clouds and files, connected rather than copied.</p></div></div>')
    hero = ('<section class="isl-hero"><div class="isl-wrap isl-hero-grid"><div>' + eyebrow('Free E-Book · For CIOs, CDOs and data leaders in Saudi Arabia') +
            f'<h1>Reliable AI starts with {g("reliable data.")}</h1><p class="isl-tagline">How ready is your data for your AI ambitions?</p>'
            '<p class="isl-lead">An AI pilot needs more than a promising idea. It needs accurate, consistent data that keeps its business meaning. This free SAP E-Book shows how SAP Business Data Cloud builds that foundation.</p>'
            f'<div class="isl-hero-ctas">{btn(BDC_MAIN + " " + ico("down"), cta="hero")}{btn("Check your data readiness", "#isl-ready", "hero-2", ghost=True)}</div><div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>{lockup()}</div>'
            f'<div class="isl-visual">{stack}</div></div></section>')
    mini = ('<div class="isl-mini isl-rv"><div><b>Scattered SAP and non-SAP data</b><p>Data sits across applications, clouds and spreadsheets, each with its own copy of the truth.</p></div><div><b>Lost business context</b><p>When data is extracted and copied, the business meaning behind it gets lost and has to be rebuilt by hand.</p></div>'
            '<div><b>Slow, manual analytics</b><p>Teams spend more time reconciling inconsistent definitions than analysing what the numbers mean.</p></div><div><b>Uncertain AI readiness</b><p>AI is only as reliable as the data behind it. Without governed, harmonized data, it is hard to trust the results.</p></div></div>')
    s_trust = section(head('The data challenge', f'Plenty of data. {g("Not enough trust.")}', 'Most organizations are not short of data. The problem is that it is scattered, stripped of context and hard to rely on when decisions and AI depend on it.') + stat_band() + mini)
    rows = ''.join(f'<div class="isl-rq"><div><b>{t}</b><span>{q}</span></div><div class="isl-yn"><button type="button" class="isl-yes" aria-pressed="false">Yes</button><button type="button" class="isl-nope" aria-pressed="false">Not sure</button></div></div>' for t, q in
                   [('Quality', 'Is the data accurate and consistent?'), ('Context', 'Are business definitions understood the same way everywhere?'), ('Access', 'Can the right people use the right data?')])
    rm = [['Start with the foundation', 'Accurate, consistent data with a shared business meaning comes before any AI pilot. The E-Book shows how SAP Business Data Cloud builds it.'],
          ['A starting point', 'Two checks are still open. Close them before you scale anything. The E-Book shows how.'],
          ['Nearly there', 'One check is still open. See how SAP Business Data Cloud keeps data governed as AI use grows.'],
          ['A strong position', 'Keep the foundation governed as AI use grows. The E-Book shows how connected data supports AI across the business.']]
    ready = (f'<div class="isl-ready isl-rv" data-ready="{jattr(rm)}">{rows}<div class="isl-rout" style="display:none"><p><b></b><span></span></p>{btn(BDC_MAIN, cta="readiness")}</div></div>')
    s_ready = section(head('Three checks before any AI pilot', f'Is your data {g("ready for AI?")}', 'Answer three quick questions. No details needed.') + ready, 'isl-pad isl-dark', 'isl-ready')
    chev = ''.join(f'<div class="isl-chev isl-rv"><small>{a}</small><b>{b}</b><span>{c}</span></div>' for a, b, c in
                   [('Connect', 'SAP and third-party sources', 'Bring them together without copying.'), ('Context', 'Harmonized data products', 'Business context is kept.'), ('Trust', 'A governed data foundation', 'Quality and access under control.'),
                    ('Insight', 'Analytics and planning', 'Decisions grounded in trusted data.'), ('Action', 'AI and decisions', 'AI that reflects how your business works.')])
    s_flow = section(head('How it works', f'From scattered data to {g("business-ready insight")}', 'SAP Business Data Cloud is a fully managed SaaS solution that unifies data and analytics. Here is how it works in business terms.') + f'<div class="isl-chev-flow">{chev}</div>', 'isl-pad isl-soft')
    out = ('<div class="isl-mini isl-three isl-rv"><div><b>Unleash transformative insights</b><p>Give business and data teams analytics and planning grounded in trusted data with its business context, so they can make decisions with confidence.</p></div>'
           '<div><b>Connect all your data</b><p>Bring SAP and third-party data together and harmonize it, without losing the semantics that make it meaningful.</p></div>'
           '<div><b>Foster reliable AI</b><p>Ground AI in governed, business-ready data so its recommendations reflect how your business actually works.</p></div></div>')
    s_out = section(head('The value of SAP Business Data Cloud', f'Three outcomes from {g("one data foundation")}', None) + out)
    tb = tabs([('Finance', '<h3>Connected planning and forecasts</h3><p>Scenario analysis and forecasts built on consistent financial and operational data, including SAP Analytics Cloud planning.</p>'),
               ('Supply chain', '<h3>A cross-functional view</h3><p>Demand, inventory and suppliers in one view, to support faster, better-informed operational decisions.</p>'),
               ('People and HR', '<h3>Workforce insight with context</h3><p>Workforce insight that combines HR data with financial and operational context.</p>'),
               ('Enterprise data', '<h3>One governed foundation</h3><p>One governed foundation for data teams to deliver trusted analytics and AI use cases at scale.</p>')])
    s_where = section(head('Where it matters', f'Better decisions {g("across the business")}', None) + tb, 'isl-pad isl-soft')
    conv = convert('paper', book=BDC_BOOK, cover_html='', toc=BDC_TOC, eyebrow_t='Free E-Book', send=BDC_SEND, sub=SUB, ok_title=BDC_OK, small_cover=cover('isl-cv-s', BDC_BOOK + ' E-Book cover'))
    conv = conv.replace('class="isl-cv-s isl-cover-src"', 'class="isl-cover-src" width="86" height="104" style="width:86px;height:auto"')
    s_why = section(why_band('Why Intrasoft', f'Your SAP partner for {g("data and analytics")}', 'Intrasoft helps organizations turn SAP data and analytics into value, from first conversation to ongoing support.', WHY))
    faq = [('What is SAP Business Data Cloud?', 'A fully managed SaaS solution from SAP that unifies data and analytics. It connects SAP and third-party data and keeps its business context, so you can use it for analytics, planning and AI.'),
           ('Does it work with non-SAP data?', 'Yes. SAP Business Data Cloud is designed to bring SAP and third-party data together. We assess your specific sources during a discovery conversation.'),
           ('How does it help with AI readiness?', 'Reliable AI needs governed, harmonized data with clear business meaning. SAP Business Data Cloud provides that foundation, so AI results reflect how your business actually works.'),
           ('Where does SAP Analytics Cloud fit in?', 'SAP Analytics Cloud provides the analytics and planning experience, including scenario analysis and rolling forecasts for finance teams.'), AFTER_DL, DATA_USE]
    s_faq = section(head('FAQ', 'Common questions') + faq_chat(faq), 'isl-pad isl-soft')
    body = '\n'.join([topbar('<b>Free E-Book:</b> reliable AI starts with reliable data.'), header(BDC_HEAD), hero, trust(), s_trust, s_ready, s_flow, s_out, s_where, conv, s_why, s_faq,
                     final(f'Check the foundation {g("before you scale.")}', 'Download the free SAP E-Book: ' + BDC_BOOK + '.', BDC_MAIN), footer(), sticky(BDC_HEAD)])
    return page('Reliable AI Starts with Reliable Data | Intrasoft', 'Reliable AI starts with reliable data. Download the free SAP E-Book on SAP Business Data Cloud, from Intrasoft, an SAP Gold Partner.', cfg, body), BDC_SEND

# ------------------------------------------------------------ V3: finance and operations (dark hero)
def bdc_v3():
    cfg = cfg_block('bdc-v3-finance-ops', BDC_PDF, PRISM, '/bdc-thank-you')
    scr = ('<div class="isl-screens" id="isl-scr"><div class="isl-scr-row">'
           f'<div class="isl-scr"><small>Finance sees</small><b>The plan</b>{bars([70, 55, 80, 62], 62)}</div><div class="isl-scr isl-ops"><small>Operations sees</small><b>What is happening</b>{bars([40, 78, 45, 90], 62)}</div><span class="isl-scr-link"></span></div>'
           '<p class="isl-screens-msg" data-msg data-off="Two views of the same business. Do they match?" data-on="Finance and operations data, connected with its business context.">Two views of the same business. Do they match?</p>'
           '<div class="isl-screens-cta"><button type="button" class="isl-btn isl-btn-ghost" data-demo="#isl-scr" data-label-off="Connect the two views" data-label-on="Show them apart again">Connect the two views</button></div></div>')
    hero = ('<section class="isl-hero"><div class="isl-wrap isl-hero-grid"><div>' + eyebrow('Free E-Book · For finance leaders in Saudi Arabia') +
            f'<h1>Can finance see {g("what operations sees?")}</h1><p class="isl-tagline">Plan for What\'s Next.</p>'
            '<p class="isl-lead">Scenario planning only works when financial plans reflect what is happening in operations. This free SAP E-Book shows how SAP Business Data Cloud connects SAP and non-SAP data, so planning, analytics and AI run on numbers everyone trusts.</p>'
            f'<div class="isl-hero-ctas">{btn(BDC_MAIN + " " + ico("down"), cta="hero")}</div><div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>'
            "<p class=\"isl-hero-note\">For CFOs, finance directors and FP&amp;A leaders in Saudi Arabia. Even if your planning relies heavily on Excel today.</p>" + lockup() + '</div>'
            f'<div class="isl-visual">{scr}</div></div></section>')
    qa = flip_cards([('What happens if revenue falls below plan?', 'Finance can <b>model the scenario</b> and compare it with the plan, on connected data rather than disconnected files.'),
                     ('What if costs rise?', 'See how rising costs affect margins, and <b>update assumptions</b> as conditions change.'),
                     ('Can we test that investment before we commit?', 'Evaluate an investment as a <b>scenario</b> and compare alternatives before the decision is made.')],
                    'Question {n}', 'With connected data', back_btn='Back to the question', front_btn='See how it works')
    s_q = section(head('What happens if…?', f'The questions leadership asks {g("finance most")}', "These aren't reporting questions. They're decisions that depend on what could happen next.") + f'<div class="isl-myths">{qa}</div>')
    chev = ''.join(f'<div class="isl-chev isl-rv"><small>{a}</small><b>{b}</b><span>{c}</span></div>' for a, b, c in
                   [('Step 1', 'Operations data', 'What is actually happening in the business.'), ('Step 2', 'Business context', 'The meaning behind the numbers is kept.'), ('Step 3', 'Finance plan', 'Plans reflect operations, not last quarter.'), ('Step 4', 'Decision', 'Alternatives compared before you commit.')])
    s_flow = section(head('Why finance and operations need one view', f'Planning is only as good as {g("the data under it")}', 'Bring finance and operations data together, with its full business context, in SAP Business Data Cloud.') + f'<div class="isl-chev-flow isl-four">{chev}</div>', 'isl-pad isl-soft')
    s_xl = section(head('Excel is not the enemy', f'Excel is not the problem. {g("Relying on it alone is.")}', 'Let us be fair to Excel. It is one of the most useful tools a finance team has.') +
                   f'<div class="isl-callout isl-rv">{ico("sheet")}<div><p><b>The trouble starts when the plan lives in many files:</b></p><ul><li>assumptions are copied, not connected</li><li>updating a forecast means updating every version</li><li>a new "what if" becomes another long planning exercise</li></ul>'
                   '<p style="margin-top:10px">The point is not replacing your tools for the sake of it. It is finding where your current process slows you down.</p></div></div>')
    tb = tabs([('CFO or Finance Director', '<h3>See potential outcomes before you decide</h3><p>You want finance to contribute to strategic discussions, not only report historical results.</p>'),
               ('Head of FP&amp;A', '<h3>More capacity for analysis</h3><p>Your team spends too long maintaining forecasts, reconciling spreadsheets and reacting to changing assumptions.</p>'),
               ('Finance transformation lead', '<h3>Technology people actually use</h3><p>You want implementation, processes, training and ongoing improvement to work together.</p>'),
               ('Rethinking planning', '<h3>Beyond the annual budget</h3><p>You want to explore rolling forecasts, driver-based planning, scenario modeling or more connected planning workflows.</p>')])
    s_pers = section(head('Who this is for', f'Built for finance leaders who need {g("more than another dashboard")}', None) + tb, 'isl-pad isl-soft')
    s = [('Assess and align', 'Agree priorities, scope and measures of success before implementation begins.'), ('Design the planning model', 'Define drivers, forecasting needs, scenarios, workflows and reporting.'),
         ('Implement with SAP Activate', 'Configure, test, validate and deploy the agreed SAP Analytics Cloud solution.'), ('Enable finance teams', 'Role-based training, participation and adoption planning.'), ('Optimize and evolve', 'Review usage, feedback and new requirements through agreed ongoing services.')]
    st = ''.join(f'<div class="isl-step isl-rv"><i>{i+1}</i><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(s))
    s_steps = section(head('Why Intrasoft is different', f'One connected journey, {g("from planning design to ongoing improvement")}', "Go-live is a milestone, not the finish line. The real objective is helping finance plan, evaluate alternatives and contribute to better business decisions.") + f'<div class="isl-steps">{st}</div>', 'isl-pad isl-dark')
    conv = convert('split', book=BDC_BOOK, cover_html=cover('isl-bigcover', BDC_BOOK + ' E-Book cover'), toc=BDC_TOC, eyebrow_t='Free E-Book', h2="Don't just prepare the next forecast.", send=BDC_SEND, sub=SUB, ok_title=BDC_OK)
    s_why = section(head('Why Intrasoft', f'Your SAP partner for {g("data and analytics")}') + why_grid([(t, p) for _, t, p in WHY]) + f'<div class="isl-why-lock isl-rv">{lockup(light=True)}</div>', 'isl-pad isl-soft')
    s_faq = section(head('FAQ', 'Common questions') + faq_acc(FIN_FAQ, one=True))
    body = '\n'.join([topbar('<b>Free E-Book:</b> can finance see what operations sees?'), header(BDC_HEAD), hero, trust(), s_q, s_flow, s_xl, s_pers, s_steps, conv, s_why, s_faq,
                     final(f'Prepare your finance team {g("for what comes next.")}', 'Download the free SAP E-Book: ' + BDC_BOOK + '.', BDC_MAIN), footer(), sticky(BDC_HEAD)])
    return page('Can Finance See What Operations Sees? | Intrasoft', 'Can finance see what operations sees? Download the free SAP E-Book on connected business data for planning, from Intrasoft.', cfg, body), BDC_SEND

# ------------------------------------------------------------ V4: impactful decisions (dark hero, CFO, second E-Book)
V4_BOOK = 'Driving Impactful Business Decisions'
V4_SEND = 'Send me the E-Book: ' + V4_BOOK
V4_HEAD = 'Get the Impactful Decisions E-Book'
V4_MAIN = 'Read the E-Book: ' + V4_BOOK
V4_OK = 'Your copy of ' + V4_BOOK + ' is ready'
def bdc_v4():
    cfg = cfg_block('bdc-v4-impactful-decisions', V4_PDF, '', '/bdc-thank-you?ebook=impactful')
    spark = lambda d: f'<svg viewBox="0 0 130 44" aria-hidden="true"><path d="{d}"/></svg>'
    tiles = ('<div class="isl-tiles" aria-hidden="true">'
             f'<div class="isl-tile"><div><small>Liquidity</small><b>Cash flow and liquidity</b><span>Visible in time to act</span></div>{spark("M2 34 L24 28 L46 32 L68 18 L90 22 L112 8 L128 12")}</div>'
             f'<div class="isl-tile isl-alert"><div><small>Receivables</small><b>Overdue payments</b><span>Surface early, with recommendations</span></div>{spark("M2 12 L24 16 L46 14 L68 26 L90 22 L112 34 L128 30")}</div>'
             f'<div class="isl-tile"><div><small>Payables</small><b>What you owe, and when</b><span>Alongside receivables and cash flow</span></div>{spark("M2 30 L24 26 L46 30 L68 24 L90 26 L112 16 L128 18")}</div></div>')
    hero = ('<section class="isl-hero"><div class="isl-wrap isl-hero-grid"><div>' + eyebrow('Free E-Book · For CFOs and finance leaders in Saudi Arabia') +
            f'<h1>Turn business data into {g("decisions, not more reports.")}</h1><p class="isl-tagline">See liquidity, receivables and payables in time to act.</p>'
            '<p class="isl-lead">Prebuilt metrics, reports and dashboards linked to live business data, so finance teams spend less time building reports and more time deciding. This free E-Book shows how intelligent content in SAP Business Data Cloud makes that possible.</p>'
            f'<div class="isl-hero-ctas">{btn(V4_MAIN + " " + ico("down"), cta="hero")}{btn("See what finance can see", "#isl-see", "hero-2", ghost=True)}</div><div class="isl-hero-meta"><span>{ico("bolt")}Instant access</span><span>{ico("check")}Free, no obligation</span></div>'
            '<p class="isl-hero-note">For CFOs, financial controllers and treasury teams in Saudi Arabia. Even if cash and receivables tracking still runs on Excel today.</p>' + lockup() + '</div>'
            f'<div class="isl-visual">{tiles}</div></div></section>')
    tb = tabs([('Liquidity', '<h3>See cash flow and liquidity without complex, multistep processes</h3><p>Intelligent content gives <b>real-time visibility</b> into liquidity, so finance can adjust financial strategies to maintain it.</p>'),
               ('Receivables', '<h3>Spot overdue payments early</h3><p>Finance can <b>quickly identify overdue payments</b> and receive tailored recommendations to improve collection rates.</p>'),
               ('Payables', '<h3>Know what you owe, and when</h3><p>Visibility into accounts payable, alongside accounts receivable and cash flow, <b>without complex, time-consuming manual work</b>.</p>')])
    s_see = section(head('What finance can see', f'Visibility {g("in time to act")}', 'Intelligent content brings liquidity, accounts receivable and accounts payable into one view.') + tb, 'isl-pad', 'isl-see')
    chev = ''.join(f'<div class="isl-chev isl-rv"><small>{a}</small><b>{b}</b><span>{c}</span></div>' for a, b, c in
                   [('Step 1', 'Connect', 'SAP and third-party data, with its business context.'), ('Step 2', 'Prebuilt content', 'Predefined metrics, reports and dashboards linked to real-time business data.'), ('Step 3', 'Decide', 'Practical insights and recommendations, so finance spends less time building reports and more time deciding.')])
    s_flow = section(head('How it works', f'From data to decision, {g("in three steps")}', None) + f'<div class="isl-chev-flow isl-three">{chev}</div>', 'isl-pad isl-soft')
    tb2 = tabs([('Finance', '<h3>Cash flow visibility and working capital</h3><p>Finance leaders can <b>improve cash flow visibility</b>, optimize working capital and adapt strategies to changing market conditions.</p>'),
                ('Supply chain', '<h3>Demand planning and inventory tracking</h3><p>Predictive analytics and real-time inventory tracking help leaders <b>anticipate customer needs</b> and identify shortages or bottlenecks early.</p>'),
                ('HR', '<h3>Attrition risks and talent gaps</h3><p>Workforce analytics help HR teams <b>identify attrition risks</b>, analyze talent gaps and target retention initiatives.</p>')])
    s_beyond = section(head('Beyond finance', f'Real-world applications {g("across the business")}', 'The E-Book walks through finance, supply chain and HR.') + tb2, 'isl-pad isl-dark')
    fnd = (f'<div class="isl-callout isl-rv">{ico("layers")}<div><p><b>Business context is a nonnegotiable ingredient for production-ready AI.</b> Intelligent content is only as powerful as the data foundation it runs on. SAP Business Data Cloud unifies data and analytics with semantically rich data from your key business processes.</p></div></div>')
    s_fnd = section(head('The foundation', f'A strong data foundation {g("comes before AI")}', None) + fnd)
    toc = [('How intelligent content gives finance real-time visibility', 'into liquidity, accounts receivable and accounts payable, so overdue payments surface early'),
           ('Why a strong data foundation with full business context', 'has to come before AI'), ('Real-world applications', 'in finance, supply chain and HR, and how to get started')]
    conv = convert('split', book=V4_BOOK, cover_html=mock_cover('SAP Business Data Cloud', 'Driving impactful business decisions with <em>intelligent content</em>'), toc=toc, eyebrow_t='Free E-Book', h2='From data to decisions, faster.', send=V4_SEND, sub=SUB, ok_title=V4_OK)
    faq = [('What is intelligent content?', 'Predefined metrics, reports and dashboards linked to real-time business data in SAP Business Data Cloud. They offer practical insights and recommendations, without complex, time-consuming manual work.'),
           ('Which areas does the E-Book cover?', 'Real-world applications in finance, supply chain and HR, the data foundation behind them, and how to get started.'),
           ('Why does the data foundation matter?', 'Intelligent content is only as powerful as the data it runs on. SAP Business Data Cloud unifies data and analytics with semantically rich data from your key business processes.'), AFTER_DL, DATA_USE]
    s_why = section(why_band('Why Intrasoft', f'Your SAP partner for {g("data and analytics")}', 'Intrasoft helps organizations turn SAP data and analytics into value, from first conversation to ongoing support.', WHY))
    s_faq = section(head('FAQ', 'Common questions') + faq_acc(faq, one=True), 'isl-pad isl-soft')
    body = '\n'.join([topbar('<b>Free E-Book:</b> turn business data into decisions, not more reports.'), header(V4_HEAD), hero, trust(), s_see, s_flow, s_beyond, s_fnd, conv, s_why, s_faq,
                     final(f'From data to decisions, {g("faster.")}', 'Download the free E-Book: ' + V4_BOOK + '.', V4_MAIN), footer(), sticky(V4_HEAD)])
    return page('Driving Impactful Business Decisions | Intrasoft', 'Turn business data into decisions, not more reports. Download the free E-Book on intelligent content in SAP Business Data Cloud, from Intrasoft, an SAP Gold Partner.', cfg, body), V4_SEND
