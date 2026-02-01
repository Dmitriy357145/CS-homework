from functools import *
@lru_cache(None)
def f(n):
    if n==1:
        return 15
    if n>=2:
        return 2*f(n-1)-n
for n in range(3000): f(n)
print((f(2025)-f(2023)-2)/2**2022)
