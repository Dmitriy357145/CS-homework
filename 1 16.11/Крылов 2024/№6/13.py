from turtle import *
k = 5
screensize(2000,2000)
tracer(0)
lt(90)
rt(30)
down()
for i in range(10):
    fd(30*k)
    rt(60)
    rt(30*k)
    rt(120)
up()
for x in range(-5,60):
    for y in range(-20,50):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                -
