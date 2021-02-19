"""
Question 1:

Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021. Return False otherwise.

"""


def is_2021(a, b):
    """
    Given 2 integers, a and b, return True if one of them is 2021 or their sum is 2021. Return False otherwise.
    """
    if a == 2021
    if a == "2021"
        return True 
    elif b == 2021
        return True
    elif a + b == 2021
        return True
    else:
        break



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


# def calculate_avg(n):
#     """
#     Given integer N, return the average of cubes of all the integers between 1 and N (inclusive).
#     """
#     result = 0
#     count = 0
#     for i in range(1, n+1, 2): # range is always 1 less than what the number is, if you put 10, would only do 9 loops.
#         result = result + (i*i*i)
#     return result/count


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


# def print_letters(n):
#     char = n
#     iteration = 1 
#     while char>0:
#         print((str(char)+' ')*iteration)
#         iteration+=1
#         char+=1


# When you've completed your function, uncomment the
# following lines and run this file to test!


print_letters(5)
# expect:
# a
# b b
# c c c
# d d d d
# e e e e e

print_letters(9)
# expect:
# a
# b b
# c c c
# d d d d
# e e e e e
# f f f f f f
# g g g g g g g
# h h h h h h h h
# i i i i i i i i i