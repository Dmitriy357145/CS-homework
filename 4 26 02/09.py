f = open('09.txt')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x)==1]
    if len(a1)==4 and a[-1]<sum(a[:-1]):
        c+=1
print(c)
