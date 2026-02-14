from turtle import *
k = 40
tracer(0)
screensize(2000,2000)
lt(90)
for i in range(2):
    fd(9*k)
    rt(90)
    fd(5*k)
    rt(270)
bk(18*k)
lt(90)
fd(10*k)
rt(90)
up()
fd(5*k)
rt(90)
fd(4*k)
lt(90)
down()
for i in range(4):
    fd(5*k)
    rt(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(5,'red')
done()
