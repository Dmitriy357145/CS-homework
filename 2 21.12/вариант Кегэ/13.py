from functools import *
@lru_cache(None)
def g(n):
    return f(n-3)

def f(n):
    if n<=20:
        return 177
    else:
        return g(n-2)+4


for n in range(22223):
    f(n)
    g(n)
print(g(22222))
