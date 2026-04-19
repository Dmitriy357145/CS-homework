f = open('09.txt')
c=0
for s in f:
    a = [int(x) for x  in s.split()]
    a3 = [int(x) for x in a if a.count(x)==3]
    a1=[int(x) for x in a if a.count(x)==1]
    if len(a3)==3 and len(a1)==3 and a3[0]*3<min(a1)**2:
        c+=1
print(a,c)
