from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
down()
for i in range(3):
    down()
    for i in range(2):
        fd(10*k)
        rt(90)
        fd(10*k)
        rt(90)
    up()
    fd(10*k)
    rt(90)
    fd(5*k)
    lt(90)

up()
for x in range(-20,22):
    for y in range(-20,40):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                100
