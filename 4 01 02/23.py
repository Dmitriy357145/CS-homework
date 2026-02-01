def f(x,y):
    if x>y:return 0
    if x==y:return 1
    res = f(x+1,y)
    c = x%10
    b = (x//10)%10
    a = x//100
    if c>b:
        r = a*100 + c*10 + b
        res +=f(r,y)
    return res
print(f(110,154))
