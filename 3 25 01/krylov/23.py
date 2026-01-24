def f(x,y):
    if x>y: return 0
    if x==y: return 1
    res = f(x+1,y)
    C = x % 10
    B = (x // 10) % 10
    A = x // 100
    if C > B:
        r = A * 100 + C * 10 + B
        res += f(r, y)
    return res
print(f(101,154))
