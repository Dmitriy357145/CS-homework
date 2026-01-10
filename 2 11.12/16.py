from functools import *
lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n%2 != 0:
        return f(n-1) - f(n-2)
    else:
        return sum(f(i) for i in range(n-1))
print(f(39))
