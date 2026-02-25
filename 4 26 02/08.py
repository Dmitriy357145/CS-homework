from itertools import *
s = []
c  = 0
for x in product('012345',repeat = 6):
    s = ''.join(x)
    if s[0] not in '0':
        if s.count('0')==1:
            s=s.replace('3','1').replace('5','1')
            if '01' not in s and '10' not in s:
                c+=1
print(s,c)
