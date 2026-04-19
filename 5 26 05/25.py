def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for x in range(500_001,10**10):
    d = div(x)
    if len(d)>0:
        f = [int(x) for x in d if x%10==3 and x!=3]
        if len(f)>0:
            k+=1
            print(x,min(f))
        if k==5: break
