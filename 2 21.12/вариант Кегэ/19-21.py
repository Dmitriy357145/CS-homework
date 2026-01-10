def f(s,c,e):
    if s <= 40 or c>e: return c%2==e%2
    h=[f(s-2,c+1,e),f(s-3,c+1,e),f(s//2,c+1,e)]
    return any(h) if (c+1)%2==e%2 else all(h)
print(19,[s for s in range(41,1000) if f(s,0,2)])
print(20,[s for s in range(41,1000) if not f(s,0,1) and f(s,0,3)])
print(21,[s for s in range(41,1000) if not f(s,0,2) and f(s,0,4)])
