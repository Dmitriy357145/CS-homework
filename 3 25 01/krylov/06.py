from  turtle import *
k = 30
tracer(0)
screensize(2000,2000)
for i in range(4):
    fd(9*k)
    lt(180)
    bk(10*k)
    rt(90)
up()
bk(7*k)
lt(90)
fd(3*k)
rt(90)
down()
for i in range(2):
    fd(17*k)
    lt(90)
    fd(20*k)
    lt(90)
up()

for x in range(-20,30):
    for y in range(-20,30):
        goto(x*k,y*k)
        dot(5,'red')
done()
