from math import *
for n in range(1,400):
    i = ceil(log2(10+26+230))
    u = ceil(i*n/8)
    if u*506 > 63 * 1024:
        print(n,i)
        break
