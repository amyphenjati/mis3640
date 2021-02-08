# exercise2.3
def greatest_common_divisor_recursive(a, b):
    """
    a, b are positive integers. function returns
    largest integer that divides each of them without remainder.
    """
    # to see the recursive pattern
    print("Current a, b:", a, b)

    # base case is when b=0
    if b == 0:
        return a
    else:
        # recursive case
        return greatest_common_divisor_recursive(b, a % b)


# test


print(greatest_common_divisor_recursive(2, 12))
print(greatest_common_divisor_recursive(6, 12))
print(greatest_common_divisor_recursive(9, 12))
print(greatest_common_divisor_recursive(17, 12))
