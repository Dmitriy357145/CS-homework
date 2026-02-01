from itertools import *
s = []
k = 0
for x in product('0123456',repeat = 4):
    s=''.join(x)
    if s[0] not in '0':
        if s[0]>s[1] and s[1]>s[2] and s[2]>s[3]:
            k+=1
            print(s,k)
