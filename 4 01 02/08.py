from itertools import *
s = []
k = 0

for x in product(sorted('СТРЕЛА'),repeat = 5):
    s = ''.join(x)
    k+=1
    if k%2!=0 and s[0] not in 'АСТ' and s.count('Е')==2 and 'ЕЕ' not in s:
        print(s,k)
