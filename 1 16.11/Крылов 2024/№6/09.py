from turtle import *
k = 5
screensize(2000,2000)
tracer(0)
lt(90)
down()
for i in range(11):
    fd(111*k)
    rt(120)
up()
for x in range(-10,98):
    for y in range(-5,115):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                5115
