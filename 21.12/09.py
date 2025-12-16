from turtle import *
tracer(0)
k = 200
lt(90)
screensize(2000,2000)
down()
begin_fill()
for i in range(3):
    fd(111*k)
    rt(120)
end_fill()
up()
cnt = 0
canvas = getcanvas()
for x in range(-300,300):
    for y in range(-300,300):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k) == (5,):
            cnt += 1
print(cnt)
done()

