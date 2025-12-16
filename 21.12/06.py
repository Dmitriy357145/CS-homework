from turtle import *
tracer(0)
k = 200
lt(90)
screensize(2000,2000)
up()
fd(100*k)
rt(90)
fd(100*k)
rt(45)
begin_fill()
down()
for i in range(4):
    fd(30*k)
    rt(90)
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

