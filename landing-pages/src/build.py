"""Regenerates the long-form pages. Usage: python3 build.py [name ...]   (no args = everything)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from components import read, HERE
import pages_gf
OUT = os.path.join(HERE, '..')
def finish(doc, send):
    return doc + read('ui.js') + '\n' + read('form.js').replace('__SEND__', send)
def gf_v1():
    import re
    from components import read as rd
    s = open(os.path.join(HERE, 'gf-v1-source.html')).read()
    css = rd('kit.css') + rd('kit2.css')
    s = re.sub(r'<style>.*?</style>', lambda m: '<style>\n' + css + '\n</style>', s, count=1, flags=re.S)
    s = s.replace('grow-fast-v1-myths-story', 'grow-fast-v1-myths')
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
    TARGETS.update({'ty-gf': ('thank-you/grow-fast.html', pages_ty.ty_gf), 'ty-bdc': ('thank-you/bdc.html', pages_ty.ty_bdc)})
except ImportError: pass
if __name__ == '__main__':
    names = sys.argv[1:] or list(TARGETS)
    for n in names:
        path, fn = TARGETS[n]
        doc, send = fn()
        out = doc if (n.startswith('ty-') or n == 'gf-v1') else finish(doc, send)
        open(os.path.join(OUT, path), 'w').write(out)
        print('built', n, '->', path, len(out))
