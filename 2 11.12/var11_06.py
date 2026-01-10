from turtle import *
tracer(0)
k = 200
screensize(2000,2000)
lt(90)
up()
fd(100*k)
rt(90)
fd(100*k)
rt(30)
down()
begin_fill()
for i in range(6):
    fd(30*k)
    rt(90)
    fd(40*k)
    rt(90)
up()
end_fill()
c = 0
canvas = getcanvas()
for x in range(-500,500):
    for y in range(-500,500):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            c += 1
print(c)
done()
