# star.py — Turtle Studio: colorful five-point star
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue"]

for point in range(5):
    t.pencolor(colors[point])
    t.forward(100)
    t.right(144)

turtle.done()
