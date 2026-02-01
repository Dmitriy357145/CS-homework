from turtle import *
k = 30
screensize(2000,2000)
tracer(0)
lt(90)
down()
for i in range(4):
    fd(19*k)
    lt(180)
    bk(10*k)
    rt(90)
up()
bk(5*k)
lt(90)
fd(4*k)
rt(90)
down()
for i in range(2):
    fd(15*k)
    lt(90)
    fd(8*k)
    lt(90)
up()
for x in range(-30,40):
    for y in range(-30,40):
        goto(x*k,y*k)
        dot(4,'red')
done()
