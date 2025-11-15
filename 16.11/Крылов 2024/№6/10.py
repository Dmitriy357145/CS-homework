from turtle import *
k = 20
screensize(2000,2000)
tracer(0)
lt(90)
down()
for i in range(10):
    fd(7*k)
    rt(120)
up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                18
