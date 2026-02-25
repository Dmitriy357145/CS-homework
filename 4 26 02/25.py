def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(700_001,701_000):
    d = div(x)
    if len(d)>0:
        s =[x for x in d if x%10==7 and x!=7]
        if len(s)>0:
            print(x,min(s))
