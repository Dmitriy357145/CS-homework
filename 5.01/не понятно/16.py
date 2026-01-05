from functools import *
@lru_cache(10)
def g(n):
    if n>=248045:
        return n/20 + 28
    if n < 248045: return g(n+9)-4

def f(n):
    if n>= 19: return f(n-4)+3580
    else: return 6*(g(n-7)-36)
for n in range(300000):
    g(n)
    f(n)
print(f(673))
