f = open('09_9-10.txt')
def g(x):
    t = sum(x)
    if t%2!=0:
        return False
    for i in range(4):
        for j in range(i+1,4):
            if x[i]+ x[j]== t//2:
                return True
           
    return False

for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0]+a[1]+a[2])/a[3] > 2 and g(a):
        print(a)
