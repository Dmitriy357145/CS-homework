def cc(x):
    s= ''
    while x>0:
        s = str(x%4)+s
        x//=4
    return s
a = []
for n in range(1,200):
    if cc(n)[-3:]=='123':
        print(cc(n)[:-3])
        a.append(n)
print(a[::-1])
