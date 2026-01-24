from itertools import *
s = []
k= 0
for x in  permutations('КАБИНЕТ'):
    s = ''.join(x)
    if s[-1] not in 'АИЕ':
        k+=1
print(k,s)
