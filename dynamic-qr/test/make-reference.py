"""
Regenerates test/reference.json: QR matrices from `segno`, used by
cross-check-segno.js to prove our matrices are byte-identical to a mature
independent implementation.

    pip install segno && python3 test/make-reference.py
"""
import json, random, string, segno

random.seed(7)
samples = [
    "https://go.example.com/menu", "https://qr.mobi/f4c17dea", "HELLO WORLD", "a",
    "https://go.example.com/m1?utm_source=qr&utm_medium=print&utm_campaign=poster",
]
for n in (5, 20, 47, 61, 120, 300, 700, 1200):
    samples.append(''.join(random.choice(string.ascii_letters + string.digits + "/:.?=&-_")
                           for _ in range(n)))

cases = []
for s in samples:
    for ec in "LMQH":
        try:
            q = segno.make(s, error=ec, mode='byte', micro=False, boost_error=False)
        except Exception:
            continue
        cases.append({"text": s, "ec": ec, "version": q.version, "mask": q.mask,
                      "size": len(q.matrix), "matrix": [list(r) for r in q.matrix]})

json.dump(cases, open('test/reference.json', 'w'))
print(f"wrote {len(cases)} cases, versions "
      f"{sorted({c['version'] for c in cases})}")
