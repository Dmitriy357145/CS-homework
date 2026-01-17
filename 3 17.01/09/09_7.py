
c = 0
f = open('09_7.txt')
for s in f:
    a = sorted([int(x) for x in s.split()])
    a3 = [x for x in a if a.count(x)==3]
    a2 = [x for x in a if a.count(x)==2]
    a1 = [x for x in a if a.count(x)==1]
    
    if len(a3)==3 and len(a2)==2 and sum(a1)/3<= a3[0]:
        c+=1
        print(a, c)
