from itertools import *
k = 0
s = []
for x in product('123456', repeat=4):
    s =''.join(x)
    if s.count('3')==1:
        s = s.replace('4','2').replace('6','2').replace('3','1').replace('5','1')
        if s.count('2')<=s.count('1'):
            k += 1
            print(k,s)
