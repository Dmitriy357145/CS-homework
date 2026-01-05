def f(a,b,c,e):
    if a*b >= 144 or c>e: return c%2==e%2
    h = [f(a+1,b,c+1,e),f(a*2,b,c+1,e),f(a,b+1,c+1,e),f(a,b*2,c+1,e)]
    return any(h) if (c+1)%2==e%2 else all(h)

print(19,[s for s in range(1,143) if f(1,s,0,2)])
print(20,[s for s in range(1,143) if not f(1,s,0,1) and f(1,s,0,3)])
print(21,[s for s in range(1,143) if not f(1,s,0,2) and f(1,s,0,4)])
