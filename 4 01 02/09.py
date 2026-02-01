f = open('09.txt')
k=0
for s in f:
   a = [int(x) for x in s.split()]
   k+=1
   a4 = [x for x in a if a.count(x)==4]
   a1 = [x for x in a if a.count(x)==1]
   if  len(a4)==4  and len(a1)==3  and sum(a4)>sum(a1):
       print(a,k)
       break
