from itertools import *
s = []
k=0
c = 0
for x in product(sorted('ФАВОРИТ'), repeat = 6):
    s = ''.join(x)
    k+=1
    if k%2==0 and s[0] not in 'О' and s.count('Р')==2:
        c+=1
print(s,c)
