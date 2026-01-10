from turtle import *
k = 6
screensize(2000,2000)
tracer(0)
lt(90)
up()
fd(100*k)
rt(90)
fd(100*k)
rt(30)
down()
for i in range(10):
    fd(20*k)
    rt(90)
    fd(30*k)
    rt(90)

up()
for x in range(80,150):
    for y in range(0,105):
        goto(x*k,y*k)
        dot(3, 'red')
done()


#                          1216
