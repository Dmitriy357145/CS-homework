a = [int(x) for x in open('17.txt')]
ans = []
def f(x):
    return 10_000<=abs(x)<100_000 and abs(x)%100==25
mx = max([int(x) for x in a if 10_000<=abs(x)<100_000 and abs(x)%100==25])
for x,y,z in zip(a,a[1:],a[2:]):
    if f(x)+f(y)+f(z)>=1 and x**2+y**2+z**2<=mx**2:
        ans.append(x**2+y**2+z**2)
print(len(ans),min(ans))
    
