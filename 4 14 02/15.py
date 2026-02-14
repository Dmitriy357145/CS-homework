def f(x,y):
    return (105!= y + 2*x) or (a>x) or (a>y)
m = []
for a in range(1,1000):
    if all(f(x,y)==1 for x in range(1,10000) for y in range(1,10000)):
        print(a)
