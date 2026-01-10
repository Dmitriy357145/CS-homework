from itertools import *
k = 0
for x in permutations('АРТЕМ'):
    s = ''.join(x)
    if s[0] not in 'АЕ' or s[-1] not in 'АЕ':
        k+= 1
        print(s,k)
