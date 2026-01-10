from turtle import *
tracer(0)
k = 200
lt(90)
screensize(2000,2000)
down()
begin_fill()
rt(60)
for i in range(4):
    fd(8*k)
    rt(120)
    fd(4*k)
    rt(240)
rt(120)
fd(2*k)
rt(90)
fd(16*(3**0.5))
rt(90)
fd(2*k)
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

