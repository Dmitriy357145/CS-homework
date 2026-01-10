for n in range(1,100):
    b = bin(n) [2:]
    if n%2==0:
        b = b + '0'
    else:
        b =b + '1'
    if b.count('1')%3 == 0:
        b = b.replace(b[:2],'11',1)
    else:
        b = b.replace(b[:2],'10',1)
    r = int(b,2)
    if r <= 37:   
        print(n,r)


#                        25
