str_1 = "laptop"
str_2 = "NatapaN"
str_3 = "BabsonCollege"


def any_lowercase1(s):
    """this function check only if first letter in the string
    is lowercase or not, then return boolean"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


print("any_lowercase1")
print(any_lowercase1(str_1))
# True or False?
print(any_lowercase1(str_2))
# True or False?
print(any_lowercase1(str_3))
# True or False?


def any_lowercase2(s):
    """Check if string 'c' is lowercase or not;
    Returns 'True' everytime, given argument does not matter."""
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"


print("any_lowercase2")
print(any_lowercase2(str_1))
# True or False?
print(any_lowercase2(str_2))
# True or False?
print(any_lowercase2(str_3))
# True or False?


def any_lowercase3(s):
    """ Result is based only on last letter of string s"""
    for c in s:
        flag = c.islower()
    return flag


print("any_lowercase3")
print(any_lowercase3(str_1))
# True or False?
print(any_lowercase3(str_2))
# True or False?
print(any_lowercase3(str_3))
# True or False?


def any_lowercase4(s):
    """ Checks if there is any lowercase letter in given string
    and returns boolean"""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print("any_lowercase4")
print(any_lowercase4(str_1))
# True or False?
print(any_lowercase4(str_2))
# True or False?
print(any_lowercase4(str_3))
# True or False?


def any_lowercase5(s):
    """returns True if ALL the
    letters in string are lowercase"""
    for c in s:
        if not c.islower():
            return False
    return True


print("any_lowercase5")
print(any_lowercase5(str_1))
# True or False?
print(any_lowercase5(str_2))
# True or False?
print(any_lowercase5(str_3))
# True or False?