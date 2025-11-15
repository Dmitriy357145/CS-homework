from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
down()
rt(180)
fd(2*k)
rt(90)
fd(30*k)
rt(90)
fd(2*k)
rt(30)
for i in range(6):
    fd(5*k)
    rt(120)
    fd(5*k)
    rt(240)
up()
for x in range(-40,20):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                101
