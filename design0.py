import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.pencolor("green")
c = 0
while True:
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.left(5)
    c += 1
    if c >= 360/5:
        break
    
t.hideturtle()
turtle.done()