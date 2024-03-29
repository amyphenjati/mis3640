def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    res: string
    """
    res = ""
    for letter in word:
        res += rotate_letter(letter, n)
    return res


# test
print(rotate_word("cheer", 7))
print(rotate_word("melon", -10))
print(rotate_word("IBM", -1))
