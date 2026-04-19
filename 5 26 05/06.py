from turtle import *
k = 80
tracer(0)
screensize(5000,5000)
lt(90)
for i in range(3):
    fd(20*k)
    rt(120)
up()
fd(5*k)
rt(60)
fd(8*k)
lt(60)
down()
for i in range(4):
    fd(30*k)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(7,'red')
done()
