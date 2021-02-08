# exercise2.2
def fibonacci(n):
    """compute the Fibonacci number of an integer , n"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# test
print(fibonacci(6))
print(fibonacci(0))
print(fibonacci(1))
