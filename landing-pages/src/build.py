"""Regenerates the long-form pages. Usage: python3 build.py [name ...]   (no args = everything)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from components import read, HERE
import pages_gf
OUT = os.path.join(HERE, '..')
def finish(doc, send):
    return doc + read('ui.js')
def gf_v1():
    import re
    from components import read as rd
    s = open(os.path.join(HERE, 'gf-v1-source.html')).read()
    css = rd('kit.css') + rd('kit2.css')
    s = re.sub(r'<style>.*?</style>', lambda m: '<style>\n' + css + '\n</style>', s, count=1, flags=re.S)
    s = s.replace('grow-fast-v1-myths-story', 'grow-fast-v1-myths')
    from components import form_block
    # drop the old form-submit script block (its handler expected the old form)
    for m in list(re.finditer(r'<script>(?:(?!</script>).)*?isl-lead-form(?:(?!</script>).)*?</script>', s, re.S))[::-1]:
        s = s[:m.start()] + s[m.end():]
    a = s.index('<form class="isl-lead-form"'); b = s.index('</form>', a) + len('</form>')
    s = s[:a] + form_block('', 'Tell us where to send it. It opens straight away, and a copy goes to your inbox.', '') + s[b:]
    return s, None
TARGETS = {
    'gf-v1': ('variants/grow-fast/v1-myths.html', gf_v1),
    'gf-v2': ('variants/grow-fast/v2-clear-answers.html', pages_gf.gf_v2),
    'gf-v3': ('variants/grow-fast/v3-growth.html', pages_gf.gf_v3),
}
try:
    import pages_bdc
    TARGETS.update({'bdc-v1': ('variants/bdc/v1-one-truth.html', pages_bdc.bdc_v1), 'bdc-v2': ('variants/bdc/v2-reliable-ai.html', pages_bdc.bdc_v2),
                    'bdc-v3': ('variants/bdc/v3-finance-operations.html', pages_bdc.bdc_v3), 'bdc-v4': ('variants/bdc/v4-impactful-decisions.html', pages_bdc.bdc_v4)})
except ImportError: pass
try:
    import pages_ty
    TARGETS.update({'ty-gf': ('thank-you/grow-fast.html', pages_ty.ty_gf), 'ty-bdc': ('thank-you/bdc.html', pages_ty.ty_bdc), 'ty-bdc-impactful': ('thank-you/bdc-impactful.html', pages_ty.ty_bdc_impactful), 'ty-booked': ('thank-you/booking-confirmed.html', pages_ty.ty_booked), 'book-call': ('thank-you/book-a-call.html', pages_ty.book_call)})
except ImportError: pass
if __name__ == '__main__':
    names = sys.argv[1:] or list(TARGETS)
    for n in names:
        path, fn = TARGETS[n]
        doc, send = fn()
        out = doc if n.startswith('ty-') else (doc + read('ui.js') if n == 'gf-v1' else finish(doc, send))
        open(os.path.join(OUT, path), 'w').write(out)
        print('built', n, '->', path, len(out))
