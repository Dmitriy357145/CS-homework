for n in range(1,100):
    x = n - n%4
    b = bin(x) [2:]
    if b.count('1')%2==0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1')%2==0:
        b = b + '0'
    else:
        b = b + '1'
    r = int(b,2)
    if r <47:
        print(n,r)


#                   11
