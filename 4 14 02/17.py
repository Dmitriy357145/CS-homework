a = [int(x) for x in open('17.txt')]
ans = []
m = min([int(x) for x in a if x%1000==500])

def g(n):
    return abs(n)%2==0
for x,y,z in zip(a,a[1:],a[2:]):
    if (x+y+z)>m and g(x)+g(y)+g(z)==0:
        ans.append(x+y+z)
print(len(ans),min(ans))
