from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
down()
rt(60)
for i in range(4):
    fd(8*k)
    rt(120)
    fd(4*k)
    rt(240)
rt(120)
fd(2*k)
rt(90)
fd(16*3**0.5*k)
rt(90)
fd(2*k)

up()
for x in range(-20,30):
    for y in range(-10,10):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                90
