def cc(x):
    s = ''
    while x>0:
        s = str(x%4) + s
        x = x//4
    return s
for n in range(1,100):
    b = cc(n)
    if n%4 == 0:
        b = b + b[-2:]
    else:
        b = b + cc(n%4*2)
    r = int(b,4)
    if r >= 1025:
        print(n,r)

#                  66
