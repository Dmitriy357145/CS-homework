f = open('09.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    k+=1
    a2=[x for x in a if a.count(x)==2]
    a1=[x for x in a if a.count(x)==1]
    if len(a2)==4 and len(a1)==2 and sum(a1)<=sum(set(a2)):
        print(a,k)

