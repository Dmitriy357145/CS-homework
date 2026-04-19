def f(x):
    P = 10<=x<=40
    Q = 20<=x<=50
    A = a1<=x<=a2
    return P <= ((Q and 1-A)<= 1-P)
ans=[]
ox =[dx for x in (10,40,20,50) for dx in (x,x+.1,x-.1)]
for a1 in ox:
    for a2 in ox:
        if a2>=a1 and all(f(x)==1 for x in ox):
            ans.append(a2-a1)
print(min(ans))
