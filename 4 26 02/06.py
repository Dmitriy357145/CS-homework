from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
for i in range(5):
    fd(30*k)
    rt(90)
    fd(40*k)
    rt(90)
up()
fd(20*k)
rt(90)
fd(5*k)
rt(90)
down()
for i in range(7):
    fd(10*k)
    rt(90)
up()
for x in range(10,50):
    for y in range(-5,30):
        goto(x*k,y*k)
        dot(4,'red')
done()
