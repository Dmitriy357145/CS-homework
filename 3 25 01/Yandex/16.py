from functools import *
@lru_cache(None)

def f(n):
    if n>=2024:
        return 1
    else:
        return f(n+2) + f(n+4)
    

    
m = []
for n  in range(5000,1,-1):
    f(n)
    m.append(f(n))
    
print(len(set(m)))

