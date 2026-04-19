a=[]
for n in range(1,10000):
    b = bin(n)[2:]
    s  = b.count('1')
    if s%3==0: b = '11' + b + '00'
    elif s%3==1: b = '10' + b + '01'
    elif s%3==2 : b =  '01'+b+'10'
    r = int(b,2)
    if r>2000:
        a.append(r)
print(min(a))
