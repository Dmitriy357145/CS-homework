from math import *
for y in range(1,100):
    x = 768*5120 * ceil(log2(256))
    if x*y/655_360 <= 500:
        print(y,x)
