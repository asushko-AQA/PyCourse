# snowflake.py — Turtle Studio: reusable branch function
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("deepskyblue")
t.width(3)


def draw_branch(length):
    t.forward(length)
    t.backward(length)


# TODO: Point upward with t.left(90)
# TODO: Call draw_branch(100)
# TODO: Turn with t.left(60)
# TODO: Call draw_branch(70)

turtle.done()
