# gallery.py
# Block 5 capstone skeleton — copy to my_gallery/gallery.py

import turtle

t = turtle.Turtle()
t.speed(0)


def draw_star():
    # TODO: colors = ["red", "orange", "gold", "green", "blue"]
    # for i in range(5): set pencolor to colors[i], forward(100), right(144)
    pass


def draw_branch(length):
    # TODO: forward(length) then backward(length)
    pass


def draw_snowflake():
    # TODO: penup, goto(200, 0), pendown, pencolor "sky blue"
    # six times: draw_branch(40) then left(60)
    pass


print("=== TURTLE GALLERY ===")
draw_star()
t.penup()
t.home()
t.pendown()
draw_snowflake()
turtle.done()
