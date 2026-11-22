# shapes.py — Turtle Studio: square and triangle
import turtle

t = turtle.Turtle()
t.speed(3)

# TODO: Draw a square. Repeat 4 times: t.forward(100) then t.left(90).

# Move right so the triangle does not sit on top of the square
t.penup()
t.forward(150)
t.pendown()

# TODO: Draw a triangle. Repeat 3 times: t.forward(100) then t.left(120).

turtle.done()
