def f(a,b,c,e):
    if a+b>=189 or c>e: return c%2==e%2
    h = [f(a+b,b,c+1,e),f(a,b+a,c+1,e)]
    if a>b:
        h.append(f(a,b+(a-b),c+1,e))
    else:
        h.append(f(a+(b-a),b,c+1,e))
    return any(h) if (c+1)%2==0 else all(h)

print(19,[s for s in range(1,184) if f(5,s,0,2)])
print(19,[s for s in range(1,184) if not  f(5,s,0,1) and f(5,s,0,3)])    
print(19,[s for s in range(1,184) if not f(5,s,0,2) and f(5,s,0,4)])
