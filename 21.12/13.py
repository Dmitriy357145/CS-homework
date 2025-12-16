from turtle import *
tracer(0)
k = 200 
lt(90)
screensize(2000,2000)
down()
begin_fill()
rt(30)
for i in range(10):
    fd(30*k)
    rt(60)
    fd(30*k)
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

