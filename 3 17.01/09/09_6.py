f= open('09_6.txt')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x)==2]
    if a[0] not in a1 and len(a1)==6:
        c+=1
        print(a,c)
