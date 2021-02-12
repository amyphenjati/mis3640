# 1
def sum_all10():
    """calculate sum of integers from 0 to 10 and
    print put result"""
    current_sum = 0

    for i in range(11):
        print(f"Iteration {i}:")
        print(f"The value of i is {i}")
        current_sum = current_sum + i
        print(f"after adding, the sum is {current_sum}")

    print(f"final result is {current_sum}")


# 2
def sum_all1000():
    """calculate sum of integers from 0 to 1000 and
    print put result"""
    current_sum = 0

    for i in range(1001):
        print(f"Iteration {i}:")
        print(f"The value of i is {i}")
        current_sum = current_sum + i
        print(f"after adding, the sum is {current_sum}")

    print(f"final result is {current_sum}")


# 3
def sum_odd():
    """calculate the sum of odd number
    from 1 to 1000, and print the sum"""
    current_sum = 0

    for i in range(1, 1001):
        print(f"Iteration{i}:")

        if i % 2 == 1:  # check if i is an odd number #for even use 0
            print(f"The value i is {i}")
            current_sum = current_sum + i
            print(f"after adding the odd number, the sum is {current_sum}")

        print()

    print(f"the final result is {current_sum}")


def main():
    sum_all10()
    sum_all1000()
    sum_odd()


if __name__ == "__main__":
    main()
