from itertools import *
s = []
k=0
for x in product(sorted('МОСКВА'),repeat = 6):
    s = ''.join(x)
    k+=1
    if k%2==0 and s[0] not in 'АВК' and s.count('К')==2 and 'КК' not in s:
        print(s,k)
        break
