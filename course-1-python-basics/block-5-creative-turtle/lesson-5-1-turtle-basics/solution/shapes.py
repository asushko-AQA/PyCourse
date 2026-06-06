# shapes.py — Turtle Studio: square and triangle
import turtle

t = turtle.Turtle()
t.speed(3)

# Square — four equal sides
for side in range(4):
    t.forward(100)
    t.left(90)

# Move right so the triangle does not overlap the square
t.penup()
t.forward(150)
t.pendown()

# Triangle — three sides, 120° turns
for side in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
