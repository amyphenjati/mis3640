"""
one simulation:
use a var for total
repeat the following step 100 times:
    roll a dice, using random
    add the value to total
print out the total

multiple simulations:
# for i in range(10):

repeat the following step 10 times:
    the simulation above
"""
import random


def simulation(n):
    """run a simulation of rolling N dice, summing up the
    value and print"""
    total = 0
    for i in range(n):
        # total +- random.randint(1, 6)
        total = total + random.randint(1, 6)
    print(total)


# simulation(100)


def multiple_simpulations(m, n):
    """run simulation M times"""
    for i in range(m):
        simulation(n)


multiple_simpulations(10, 100)
