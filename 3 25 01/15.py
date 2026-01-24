def f(x):
    B = 101<=x<=143
    C = 144<=x<=199
    A = a1<=x<=a2
    return A<=(B or C)
ox = [dx for x in(101,143,144,199) for dx in (x,x+0.0001,x-0.0001)]
m = []
for a1 in ox:
    for a2 in ox:
        if a2>=a1 and all(f(x)==1 for x in ox):
            m.append(a2-a1)
            print(max(m), a1,a2)
        
