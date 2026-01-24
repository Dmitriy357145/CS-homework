f = open('09.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if ((a[1]+a[2]+a[3])/3)>=8:
        k+=1
print(a,k)
        
