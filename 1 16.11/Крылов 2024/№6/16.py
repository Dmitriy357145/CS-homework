from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
down()
rt(90)
fd(4*k)
rt(90)
fd(48*k)
rt(90)
fd(4*k)
rt(30)
for i in range(8):
    fd(6*k)
    rt(120)
    fd(6*k)
    rt(240)
up()
for x in range(-20,20):
    for y in range(-50,10):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                285
