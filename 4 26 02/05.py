for n  in  range(1,100):
    b = bin(n)[2:]
    if n%2==0:
        b  = b.replace('1','11',)
    else:
        b  = b.replace('0','00',)
    r = int(b,2)
    if r>70:
        print(n,r)
