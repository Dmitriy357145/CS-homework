from turtle import *
tracer(0)
k = 200
lt(90)
screensize(2000,2000)
down()
begin_fill()
for i in range(10):
    rt(120)
    fd(12*k)
    rt(60)
    fd(12*k)
end_fill()
up()
cnt = 0
canvas = getcanvas()
for x in range(-500,500):
    for y in range(-500,500):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            cnt += 1
print(cnt)
done()

