# exercise3
import math


def mysqrt(a):
    """
    use Newton’s method to compute square root of a number.
    """
    epsilon = 0.0000001
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def test_square_root():
    """
    compare the square root of integers with newton's method
    """
    # make a comparison table
    print("a   mysqrt(a)      math.sqrt(a)   diff")
    print("-   ---------      ------------   ----")
    for a in range(1, 10):
        print(
            f"{a:.1f} {mysqrt(a)::<.12f} {math.sqrt(a):<.12f} {abs(mysqrt(a) -math.sqrt(a))}"
        )
    # i can't get the format of the table to identical to the given table;
    # no idea how to do it


def main():
    test_square_root()


if __name__ == "__main__":
    main()
