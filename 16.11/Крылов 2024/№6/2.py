from turtle import *
k = 15
screensize(2000,2000)
tracer(0)
lt(90)
down()
for i in range(2):
    fd(15*k)
    lt(90)
    fd(20*k)
    lt(90)
up()
rt(90)
bk(7*k)
lt(90)
fd(9*k)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(15*k)
    rt(90)

up()
for x in range(-20,20):
    for y in range(-20,40):
        goto(x*k,y*k)
        dot(3, 'red')
done()


#                      584
