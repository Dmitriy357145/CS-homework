from itertools import *
c = 0
for x in product(sorted('АТОМ'),repeat = 4):
    s = ''.join(x)
    c+=1
    if s[0] in 'О':
        print(c)
        break
