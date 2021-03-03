import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size+1, angle+1, shift+1 )

t.bgcolor('black')
t.speed('fast')
t.pensize(5)

t.pencolor('red')
draw_circle(30, 0, 1)
