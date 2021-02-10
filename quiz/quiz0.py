"""
Question 1:
Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
Weight on Moon = weight on Earth * 0.165
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def calculate_weight_on_moon():
    """prompts user to input values for weight on earth, converts them to
    weight on moon."""
    #enter mooon weight and convert 
    weight_on_earth = float(input("Enter your weight (kg): "))
    #equation
    weight_on_moon = float(weight_on_earth) * 0.165

    #return calculated
    return weight_on_moon


print("Your weight on the Moon is: ", calculate_weight_on_moon())
