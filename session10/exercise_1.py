prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':  # if the letter is O or Q
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)