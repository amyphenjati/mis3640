"""
Question 1:
Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
Weight on Moon = weight on Earth * 0.165
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


moonweight_multiple = 0.165


def calculate_weight_on_moon():
    """prompts user to input values for weight on earth, converts them to
    weight on moon."""
    # enter earth weight
    weight_on_earth = float(input("Enter your weight (kg): "))
    # equation
    weight_on_moon = (weight_on_earth) * moonweight_multiple
    # calculated result
    print(f"Your weight on moon is {weight_on_moon}")


# test if function works
calculate_weight_on_moon()


"""
Question 2:
Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.
Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Venus = weight on Earth * 0.904
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

moon_multiple = 0.165
mars_multiple = 0.378
venus_multiple = 0.904


def weight_on_planet(weight, planet):
    """defines weight on each planet by using weight on earth"""
    # moon
    if planet == "moon":
        moon_weight = weight * moon_multiple
        return f"You weight on {planet} is {moon_weight}"

    # mars
    elif planet == "mars":
        mars_weight = weight * mars_multiple
        return f"You weight on {planet} is {mars_weight}"

    # venus
    elif planet == "venus":
        venus_weight = weight * venus_multiple
        return f"You weight on {planet} is {venus_weight}"
    else:
        return 0


# test
print(weight_on_planet(50, "moon"))
