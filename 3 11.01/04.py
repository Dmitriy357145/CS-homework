from itertools import *
from collections import *
def f(codes):
    s=sorted(codes)
    return all(not b.startswith(a) for a,b in zip(s,s[1:]))

text = 'ПАРАЛЛЕЛЬ'
fixed = {'Л':'0'}

ordered = [ch[0] for ch in Counter(text).most_common() if ch[0] not in fixed]

ac = sorted([code for ln in range(1,6)
             for code in map(''.join,product('01',repeat = ln))
             if f([code,*fixed.values()])], key = len)
ans = float('inf')
best = []
for combo in combinations(ac,len(ordered)):
    cur = dict(zip(ordered,combo),**fixed)
    if f(cur.values()):
        total = sum(len(cur[c]) for c in text[:])
        if total<ans:
            ans = total
            best = cur
print(ans,dict(sorted(best.items())))
