#  exercise 1


def sumall(*args):
    """takes any number of arguments and returns their sum."""
    return sum(args)



def main():
    print(sumall(1, 2, 3))
    print(sumall(1, 2, 3, 4, 5))
    print(sumall(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

if __name__ == "__main__":
    main()
