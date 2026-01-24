from math import *
for x in range(1,40000):
    i = ceil(log2(10+70))
    u = ceil(i*x/8)
    
    if u*1234567>24*1024*1024:
        print(x)
        break
