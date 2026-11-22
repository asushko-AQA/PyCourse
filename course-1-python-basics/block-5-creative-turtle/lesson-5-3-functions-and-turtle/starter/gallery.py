# gallery.py
# Block 5 capstone skeleton — copy to my_gallery/gallery.py

import turtle

t = turtle.Turtle()
t.speed(0)


def draw_star():
    # TODO: Five-point star — loop 5 times, not 6
    # colors: red, orange, gold, green, blue
    # each step: set pencolor, forward(100), right(144)
    pass


def draw_branch(length):
    # TODO: Go forward by length, then backward by the same length
    pass


def draw_snowflake():
    # TODO: Lift the pen, goto(200, 0), put the pen down
    # TODO: Set a sky-blue pencolor
    # TODO: Six times: draw_branch(60), then left(60)
    pass


print("=== TURTLE GALLERY ===")
draw_star()
draw_snowflake()
turtle.done()
