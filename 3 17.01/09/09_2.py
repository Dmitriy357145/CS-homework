f =open('09_2.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if len(a)==len(set(a)) and a[3]< a[0]+a[1]+a[2]:
        k+=1
print(k,a)
