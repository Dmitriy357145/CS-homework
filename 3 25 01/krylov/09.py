f = open('09.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a3 = [x for x in a if a.count(x)==3]
    a1 = [ x for x in a if a.count(x)==1]
    k+=1
    if len(a3)==3 and len(a1)==4 and sum(a1)>sum(a3):
        
        print(k,a)
