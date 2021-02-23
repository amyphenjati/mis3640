"""
Question 1:

Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021. Return False otherwise.

"""


def is_2021(a, b):
    """
    Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021. Return False otherwise.
    """
    if a == 2021 or b == 2021 or a + b == 2021:
        return True
    else:
        return False


# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(is_2021(2021, 2))
# # expect: True
# print(is_2021(2, 2021))
# # expect: True
# print(is_2021(2000, 21))
# # expect: True
# print(is_2021(2020, 21))
# # expect: False

"""
-----------------------------------------------------------------------
Question 2:

Write a function with loop(s) that computes the average of cubes of all
integers between 1 and n (inclusive). 
For example: if n is 5, the average is (1*1*1 + 2*2*2 + ... + 5*5*5)/5 = 45 
"""


def calculate_avg(n):
    """
    computes the average of cubes of all
    integers between 1 and n (inclusive)"""
    count = 0
    for i in range(1, n + 1):
        average_of_cubes = i * i * i
        count += average_of_cubes
    return count / n


# # When you've completed your function, uncomment the
# # following lines and run this file to test!


# print(calculate_avg(1))
# # expect: 1.0
# print(calculate_avg(5))
# # expect: 45.0


"""
-----------------------------------------------------------------------
Question 3:

Write a function with loop that prints the following pattern.
If n is 5, expected output is:

a 
b b 
c c c 
d d d d 
e e e e e 

Hint: use ord() and chr()

If it is difficult for you, try to print the following pattern first:
1
22
333
4444
55555
"""


def print_letters(n):
    """Function to demonstrate printing pattern of alphabets"""

    # initializing value corresponding to 'a'
    num = 97

    # outer loop to print number of rows, n
    for i in range(0, n):

        # inner loop for number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):

            # converting to char
            ch = chr(num)

            # printing char value
            print(ch, end=" ")

        # incrementing number
        num += 1

        # ending line after each row
        print()


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print_letters(5)
# # expect:
# # a
# # b b
# # c c c
# # d d d d
# # e e e e e

# print_letters(9)
# # expect:
# # a
# # b b
# # c c c
# # d d d d
# # e e e e e
# # f f f f f f
# # g g g g g g g
# # h h h h h h h h
# # i i i i i i i i i