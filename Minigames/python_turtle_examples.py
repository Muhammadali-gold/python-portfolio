from turtle import *

def func1(turtle1):
    colors = ['red', 'purple', 'blue', 'green', 'orange']
    for x in range(150):
        turtle1.pencolor(colors[x % 5])
        turtle1.width(x/10 + 1)
        turtle1.forward(x)
        turtle1.left(59)

def func2(turtle2):
    for i in range(200):
        turtle2.forward(i)
        turtle2.left(91)

def fun3():
    t1 = Turtle()
    t1.speed(0)
    func1(t1)
    t2 = Turtle()
    t2.speed(0)
    t2.penup()
    t2.forward(260)
    t2.pendown()
    func2(t2)

def func4():
    turtle1 = Turtle()
    turtle1.pendown()
    circle_size = 100
    for i in range(6):
        turtle1.circle(circle_size)
        turtle1.left(60)

def func5():
    turtle1 = Turtle()
    for angle in range(0, 360, 20):
        turtle1.setheading(angle)
        turtle1.forward(100)
        turtle1.write(str(angle) + '*')
        turtle1.backward(100)

# Main
func5()
