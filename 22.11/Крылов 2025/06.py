from turtle import *
k = 15
tracer (0)
screensize(2000,2000)
lt(90)
for i in range(3):
    down()
    for i in range(2):
        fd(10*k)
        rt(90)
        fd(10*k)
        rt(90)
    up()
    fd(5*k)
    rt(90)
    fd(5*k)
    lt(90)
up()
for x in range(-5,30):
    for y in range(-4,30):
        goto(x*k,y*k)
        dot(3,'red')
done()
