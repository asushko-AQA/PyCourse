# gallery.py
# Block 5 capstone skeleton — copy to my_gallery/gallery.py

import turtle

t = turtle.Turtle()
t.speed(0)


def draw_star():
    # TODO: Loop 6 times — forward 100, left 144, change pencolor
    colors = ["red", "orange", "gold", "green", "blue", "purple"]
    for i in range(6):
        t.pencolor(colors[i % len(colors)])
        t.forward(100)
        t.left(144)


def draw_branch(length):
    # TODO: forward then backward
    t.forward(length)
    t.backward(length)


def draw_snowflake():
    # TODO: Move right, draw 6 branches with left(60) between
    t.penup()
    t.goto(120, 0)
    t.pendown()
    t.pencolor("sky blue")
    for _ in range(6):
        draw_branch(40)
        t.left(60)


print("=== TURTLE GALLERY ===")
draw_star()
t.penup()
t.home()
t.pendown()
draw_snowflake()
turtle.done()
