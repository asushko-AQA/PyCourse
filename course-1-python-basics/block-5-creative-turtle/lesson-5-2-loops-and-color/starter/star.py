# star.py — Turtle Studio: colorful five-point star
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue"]

# TODO: Loop 5 times — set pencolor, forward(100), right(144)
for point in range(5):
    t.pencolor(colors[point])
    t.forward(100)
    t.right(144)

turtle.done()
