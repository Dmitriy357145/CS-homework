from itertools import *
s = []
c = 0
for x in product('01234',repeat = 5):
    s = ''.join(x)
    if s[0] not in '0':
        if s.count('3')==1 and '03' not in s and '30' not in s:
            c+=1
print(s,c)
