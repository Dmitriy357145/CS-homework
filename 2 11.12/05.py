for n in range(1,100):
    b = bin(n)[2:]
    if len(b)%2 == 0:
        i = len(b)//2
        b = b[:i] + '1' + b[i:]
    else:
        b = b
    r = int(b,2)
    print(n,r)
