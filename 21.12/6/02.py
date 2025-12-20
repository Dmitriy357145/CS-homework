from turtle import *
tracer(0)
k = 10
lt(90)
screensize(2000,2000)
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
cnt = 0
canvas = getcanvas()
for x in range(-70,70):
    for y in range(-70,70):
        goto(x*k,y*k)
        dot(3,'red')
print(cnt)
done()
