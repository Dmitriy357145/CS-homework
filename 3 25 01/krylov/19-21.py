def f(s,c,e):
    if s <= 60 or c>e: return  c%2==e%2
    h = [f(s-3,c+1,e),f(s-5,c+1,e),f(s//4,c+1,e)]
    return any(h) if (c+1)%2==e%2 else all(h)
print([s for s in range(61,500) if f(s,0,2)])
print([s for s in range(61,500) if not f(s,0,1) and f(s,0,3)])
print([s for s in range(61,500) if not f(s,0,2) and f(s,0,4)])
