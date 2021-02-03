def my_abs(number):
    # this function returns absolute value of integers and floating numbers
    if isinstance(number, (int, float)):
        if number < 0:
            return -number
        else:
            return number
    else:
        # not float or integer
        print("Invalid Input")


# test
print(my_abs(-324))
print(my_abs("a"))
print(my_abs(23))
