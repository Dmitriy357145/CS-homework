from math import *
for x in range(1,100):
    i = ceil(log2(x))
    u = ceil(i*23/8)
    if u*3_222_444 >= 45 *1024*1024:
        print(x)
