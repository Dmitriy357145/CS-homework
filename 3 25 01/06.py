from turtle import  *
k = 50
screensize(2000,2000)
tracer(0)
down()
lt(90)
for i in range(6):
    fd(7*k)
    rt(120)
up()
fd(3*k)
rt(90)
down()
for i in range(8):
    fd(5*k)
    rt(90)

up()
for x in range(-10,30):
    for y in range(-10,30):
        goto(x*k,y*k)
        dot(5,'red')
done()
