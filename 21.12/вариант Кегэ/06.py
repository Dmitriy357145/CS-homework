from turtle import *
from math import *
k = 10
screensize(2000,2000)
tracer(0)
lt(90)
down()
fd(5*k)
rt(60)
for i in range(6):
    fd(23*k)
    rt(45)
    fd(17*k)
    rt(135)
lt(90)
fd(7*k)
up()
print(sin(radians(45))*23*17)

done()
