from math import *
for x in range(1,100):
    i = ceil(log2(10+52+3))
    u10 = (ceil(10*i/8)+x)*10
    u5 = (ceil(20*i/8)+x)*5
    if u5+u10<300:
        print(x)
