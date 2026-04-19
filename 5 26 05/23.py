def f(x,y):
    if x>y or x==20: return 0
    if x==y: return 1
    return f(x+1,y)+f(x+5,y)+f(x*5,y)
print(f(3,10)*f(10,25))

62
