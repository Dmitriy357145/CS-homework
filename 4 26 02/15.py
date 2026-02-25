m = []
def f(x):
    return ((x%9==0) <= (x%6!=0)) or (x+a>=100)

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,1_000_00)):
        m.append(a)
print(min(m))
