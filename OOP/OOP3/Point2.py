class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        """
        return a Point object in a human-readable format
        """
        return f"{self}: ({self.x},{self.y})"
        # when I return f"{self}: ({self.x},{self.y})" in the __str__ method, it says maximum recursion depth occurred. why?


p1 = Point(3, 4)
# print(p1.x, p1.y)

print(p1)  # what if we want to print p1 nicely

p2 = Point(5)
print(p2)
# print(p2.x, p2.y)