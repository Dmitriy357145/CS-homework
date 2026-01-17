from itertools import *
s = []
k =0
for x in product('123456',repeat = 5):
    s = ''.join(x)
    if s.count('3')==1:
        s = s.replace('3','1').replace('5','1').replace('4','2').replace('6','2')
        if s.count('2')<=s.count('1'):
            k += 1
            print(s,k)
