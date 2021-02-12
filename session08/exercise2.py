# 1
def sum_all10_while():
    """calculate sum of integers from 0 to 10 using while loop"""
    n = 0
    sum = 0
    while n <= 10:
        sum += n
        n += 1
    print(sum)


# 2
def sum_all1000_while():
    """calculate sum of integers from 0 to 1000 using while loop"""
    n = 0
    sum = 0
    while n <= 1000:
        sum += n
        n += 1
    print(sum)


# 3
def sum_odd_while():
    """calculate sum of all odd integers from 0 to 1000  using while loop"""
    n = 0
    sum = 0
    while n <= 1000:
        if n % 2 == 1:
            sum += n
        n += 1
    print(sum)


def main():
    sum_all10_while()
    sum_all1000_while()
    sum_odd_while()


if __name__ == "__main__":
    main()
