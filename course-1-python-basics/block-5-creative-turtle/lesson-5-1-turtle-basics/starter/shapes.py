# shapes.py — Turtle Studio: square and triangle
import turtle

t = turtle.Turtle()
t.speed(3)

# TODO: Draw a square — forward(100) and left(90) four times
for side in range(4):
    t.forward(100)
    t.left(90)

# Move right so the triangle does not sit on top of the square
t.penup()
t.forward(150)
t.pendown()

# TODO: Draw a triangle — forward(100) and left(120) three times
for side in range(3):
    t.forward(100)
    t.left(120)

# TODO: Keep the window open — uncomment the line below if the window closes too fast
turtle.done()
