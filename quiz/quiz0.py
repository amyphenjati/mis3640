"""
Question 1:
Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
Weight on Moon = weight on Earth * 0.165
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


# def calculate_weight_on_moon():
#     """prompts user to input values for weight on earth, converts them to
#     weight on moon."""
#     #enter mooon weight and convert 
#     weight_on_earth = float(input("Enter your weight (kg): "))
#     #equation
#     weight_on_moon = float(weight_on_earth) * 0.165

#     #return calculated
#     return weight_on_moon


# print(f'Your weight on the Moon is: ", {calculate_weight_on_moon()}')

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


def weight_on_planet (weight, planet):
    """defines weight on each planet by using weight on earth"""
    #moon
    if planet == "moon":
        moon_weight = weight * 0.165
        return(f'You weight on {planet} is {moon_weight}')

    #mars
    elif planet == "mars":
        mars_weight = weight * 0.378
        return(f'You weight on {planet} is {mars_weight}')

    #venus
    elif planet == "venus":
        venus_weight = weight * 0.904
        return(f'You weight on {planet} is {venus_weight}')

#test
print(weight_on_planet(50, "moon"))

