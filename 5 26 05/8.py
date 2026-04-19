from itertools import *
k=0
def f(n):
    return int(str(n),16)**0.5 in [2,3,4,5,6,7,8,9]
for x in product('0123456789ABCDEF',repeat = 4):
    s=''.join(x)
    if s[0]!=0:
        if int(str(s),16)%8==0 and f(s[0])+f(s[1])+f(s[2])+f(s[3])==2:
            for c in '0123456789ABCDEF':
                if s.count(c)<=2:
                    if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3]:
                        k+=1
print(s,k)
        
                        
                   
