# exercise1.1.1

def check_fermat(a, b, c, n):
    """takes four parameters — a, b, c and n — and checks to see if Fermat’s
    theorem holds"""
    if n > 2 and (a ** n + b ** n == c ** n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


# exercise1.1.2

def check_fermat_inputs():
    """prompts the user to input values for a, b, c and n, converts them to
    integers, and uses check_fermat to check whether they violate Fermat’s
    theorem"""
    print("enter a, b, c and n to check Fermat's theorem:")
    a = int(input("Please enter integer a: "))
    b = int(input("Please enter integer b: "))
    c = int(input("Please enter integer c: "))
    n = int(input("Please enter integer (>2) n: "))

    check_fermat(a, b, c, n)


print(check_fermat_inputs())


# exercise1.2.1


def calculate_bmi(weight, height):
    """return BMI based on weight and height"""
    bmi = weight / (height * height)
    return bmi


# exercise1.2.2

def get_bmit_category():
    """prompts user to input values for weight and height, converts them to
    floats, uses calculate_bmi to calculate BMI value, and prints the
    corresponding BMI category."""
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        print(f"Your bmi is {bmi:.1f}. You are underweight.")
    elif 18.5 <= bmi <= 24.9:
        print(f"Your bmi is {bmi:.1f}. You are normal weight.")
    elif 25 <= bmi <= 29.9:
        print(f"Your bmi is {bmi:.1f}. You are overweight.")
    else:
        print(f"Your bmi is {bmi:.1f}. You are obese.")


print(get_bmit_category())
