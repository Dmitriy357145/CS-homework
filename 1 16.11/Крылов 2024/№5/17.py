for n in range(1,100):
    x = n - n%8 + n%2
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
    if r > 90:
        print(n,r)


#                   96
