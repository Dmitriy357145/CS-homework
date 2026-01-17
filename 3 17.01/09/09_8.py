f = open('09_8.txt')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a4 = [x for x in a if a.count(x)==4]
    a2 = [x for x in a if a.count(x)==2]
    a1 = [x for x in a if a.count(x)==1]
    if len(a4)==4 and len(a2)==2 and sum(a1)/2 >= max(a4[0],a2[0]):
        c += 1
        print(a,c)
