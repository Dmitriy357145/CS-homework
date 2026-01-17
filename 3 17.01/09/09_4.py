f = open('09_4.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x)==2]
    if len(a1)==2 and (a[1]<30 or a[2]<30):
        k+=1
        print(k,a)
