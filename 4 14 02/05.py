for k in range(1000,10000):
    s = sum([int(x) for x in str(k)])
    m = max([int(x) for x in str(k)])
    n = min([int(x) for x in str(k)])
    p1= str(s-m)
    p2= str(s-n)
    if p1>p2:
        l = p2+p1
    else:
        l = p1+p2
    if l == '1318':
        print(l,k)
