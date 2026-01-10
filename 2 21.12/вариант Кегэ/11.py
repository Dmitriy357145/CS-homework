from math import *
for x in range(1,100):
    i = ceil(log2(10+8182))
    u = ceil(i*12/8)
    U = u + x
    if U*600 == 50.390625*1024:
        print(x)
