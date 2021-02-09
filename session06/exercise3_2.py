import turtle
from refactoring import arc, circle, move


def yinyang(t):
    """draw ying yang symbol"""
    # main circle
    circle(t, 100)

    # bottom arc - move pen to center and draw down an arc
    move(t, 0, 100)
    t.setheading(180)
    arc(t, 50, 180)

    # top arc - move pen to center and draw an arc
    move(t, 0, 100)
    t.setheading(0)
    arc(t, 50, 180)

    # bottom small circle
    move(t, 0, 50 + 100 / 5)
    circle(t, 100 / 5)

    # top small circle
    move(t, 0, 150 + 100 / 5)
    circle(t, 100 / 5)


t = turtle.Turtle()
print(yinyang(t))
turtle.mainloop()
