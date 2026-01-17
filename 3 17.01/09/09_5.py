f = open('09_5.txt')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a3 = [x for x in a if a.count(x)==3]
    a1 = [x for x in a if a.count(x)==2]
    if len(a3)==6 and len(a1)==0 and s[-1] not in a3:
        c+=1
        print(a,c)
