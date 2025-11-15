for n in range(1,100):
    b = bin(n)[2:]
    b = b.replace('1','11',)
    b =b.replace('0','00',)
    r = int(b,2)
    if r > 63:
        print(n,r)

#                   192
