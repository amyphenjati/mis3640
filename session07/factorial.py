# exercise2.1
def factorial(n):
    """compute a factorial of an integer, n"""
    if n == 0:
        return 1
    elif n < 0:
        print("factorial does not exist for a negative number")
    else:
        return n * factorial(n - 1)


# test
print(factorial(10))
print(factorial(1))
print(factorial(0))
print(factorial(-1))
