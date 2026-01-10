from turtle import *
k = 15
tracer(0)
screensize(2000,2000)
lt(90)
down()
for i in range(5):
    fd(35*k)
    rt(90)
    fd(24*k)
    rt(90)
up()
rt(90)
fd(7*k)
rt(90)
fd(5*k)
down()
for i in range(1001):
    rt(90)
    fd(20*k)
    rt(90)
    fd(36*k)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(4,'red')
done()
