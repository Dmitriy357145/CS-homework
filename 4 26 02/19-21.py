def f(s,c,e):
    if s<=31 or c>e: return c%2==e%2
    h = [f(s-2,c+1,e),f(s-5,c+1,e),f(s//3,c+1,e)]
    return any(h) if (c+1)%2==e%2 else all(h)
for e in 2,3,4:
    print(e,[s for s in  range(32,400) if  f(s,0,e) and not f(s,0,e-2)])
