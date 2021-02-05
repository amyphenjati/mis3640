import math


def quadratic(a, b, c):
    """function for finding roots of quadratic equation"""
    # if a = 0 then it's not a quadratic formula
    if a == 0:
        print("Invalid quadratic formula")
        return None

    # calculate discriminant
    d = b ** 2 - 4 * a * c

    # equation with real solutions
    if d >= 0:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        return x_1, x_2

    # when discriminant is less than 0, there is no real solution
    else:
        print("The roots are imaginary solutions")
        return None

#test
print(quadratic(1,2,1))
print(quadratic(1,4,5))
print(quadratic(1,5,6))