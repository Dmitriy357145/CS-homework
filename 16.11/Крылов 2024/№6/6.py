from turtle import *
k = 7
screensize(2000,2000)
tracer(0)
lt(90)
up()
fd(100*k)
rt(90)
fd(100*k)
rt(45)
down()
for i in range(10):
    fd(30*k)
    rt(90)
up()
for x in range(75,140):
    for y in range(10,110):
        goto(x*k,y*k)
        dot(3, 'red')
done()

#                882
