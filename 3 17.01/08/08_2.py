from itertools import *
k = 0
s = []
for x in product('012345', repeat=7):
    s =''.join(x)
    if s[0] not in '0':
        s = s.replace('3','1').replace('5','1')
        if s.count('0')==1 and ('01' not in s and '10' not in s):
            k += 1
print(k,s)
