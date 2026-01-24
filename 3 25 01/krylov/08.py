from itertools import  *
s = []
k = 0
for x in product('СТРЕЛА', repeat =5):
    s = ''.join(x)
    k+=1
    if s[0] not in 'АСТ' and s.count('Л')==2 and 'ЛЛ' not in s and k%2==0:
        print(k,s)
