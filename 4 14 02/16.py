def f(n):
    if n<10:
        return n
    if n>=10:
        return n**3 + f(n-15)
print(f(1000)-f(940))
