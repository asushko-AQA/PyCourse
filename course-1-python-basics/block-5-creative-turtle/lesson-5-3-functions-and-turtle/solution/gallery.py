# gallery.py
# Block 5 capstone — star + snowflake in one Turtle Studio show
# Copy to my_gallery/gallery.py at your project root

import turtle

t = turtle.Turtle()
t.speed(0)


def draw_star():
    colors = ["red", "orange", "gold", "green", "blue", "purple"]
    for i in range(6):
        t.pencolor(colors[i % len(colors)])
        t.forward(100)
        t.left(144)


def draw_branch(length):
    t.forward(length)
    t.backward(length)


def draw_snowflake():
    t.penup()
    t.goto(120, 0)
    t.pendown()
    t.pencolor("sky blue")
    for _ in range(6):
        draw_branch(40)
        t.left(60)


print("=== TURTLE GALLERY ===")
print("Drawing your star and snowflake...")

draw_star()

t.penup()
t.home()
t.pendown()

draw_snowflake()

turtle.done()
