from turtle import *
k = 200
screensize(2000,2000)
tracer(0)
lt(90)

begin_fill()
down()
for i in range(3):
    fd(111*k)
    rt(120)
end_fill()

up()
canvas = getcanvas()
c = 0
for x in range(-500,500):
    for y in range(-500,500):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            c += 1
print(c)
done()

