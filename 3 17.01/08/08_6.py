from itertools import *
s = []
c = 0
k =0
for x in product(sorted('РЕПЛИКА'),repeat  = 6):
    s =''.join(x)
    c +=1
    if c%2==0 and s[0] not in 'К' and s.count('И')>=2:
        k+=1
print(s,k)
