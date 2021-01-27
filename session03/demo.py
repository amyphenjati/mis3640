# output

print("arguement")
print("arguement1", "areguement2")
print("don't")
# \: escape charater
# \': '
# \t: a tab
print("The total number of overall medals in Rio 2016 is", 46 + 37 + 38)
print("46 + 37 + 38 =", 46 + 37 + 38)

#input

name = input('type something:')
print(name)

n=100
print(n)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

#string operation
first_name = 'John'
last_name = 'Lennon'
print(first_name +' '+ last_name)

print('Naah, na na nanana naah, nanana naah, hey Jude.\n ' * 10)
# \n: new line

print(f'hello, {name}')

pi = 3.1415926

print(f'Pi equals {pi:.5f}.')
print(f'Pi equals {pi:8.5f}.')
print(f'Pi equals {pi:8.2f}.')

a = 2020

# binary
print(f'{a:b}')

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")