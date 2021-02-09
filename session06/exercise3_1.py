import turtle
from refactoring import arc, circle, move


def section(t, r, angle):
    """Draws a section of inside shape using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: degree that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def inside_shape(t, n, r, angle):
    """Draws the inside shape with n sections.
    t: Turtle
    n: number of sections
    r: radius of the arcs
    angle: side that subtends the arcs
    """
    for i in range(n):
        section(t, r, angle)
        t.lt(360.0 / n)

# combine all shape


def shape():

    # draw main circle
    circle(t, 120)
    move(t, 0, 120)

    # draw inside shape
    inside_shape(t, 6, 120, 60.0)


# draw final shape
t = turtle.Turtle()

print(shape())
turtle.mainloop()
