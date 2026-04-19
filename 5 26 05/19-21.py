def f(s,c,e):
    if s>=77 or c>e: return c%2==e%2
    h = [f(s+1,c+1,e),f(s+4,c+1,e),f(s*2,c+1,e)]
    return any(h) if (c+1)%2==e%2 else all(h)
for e in 2,3,4:
    print(e,[s for s in range(1,78) if f(s,0,e-2)<f(s,0,e)])
