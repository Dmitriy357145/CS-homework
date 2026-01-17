from itertools import *
s = []
k = 0
for x in product('01234567',repeat = 5):
    s = ''.join(x)
    if s[0] not in '0':
        s = s.replace('3','1').replace('5','1').replace('7','1')
        if '14' not in s and '41' not in s and s.count('4')==2:
            k+=1
            print(s,k)
