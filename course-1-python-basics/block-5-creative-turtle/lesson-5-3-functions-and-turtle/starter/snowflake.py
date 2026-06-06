# snowflake.py — Turtle Studio: reusable branch function
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("deepskyblue")
t.width(3)


def draw_branch(length):
    t.forward(length)
    t.backward(length)


# TODO: Point upward, call draw_branch twice, turn left between calls
t.left(90)

draw_branch(100)

t.left(60)
draw_branch(70)

turtle.done()
