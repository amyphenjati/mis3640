# exercise 3


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    word: string
    returns: boolean
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False


def find_triple_double():
    """prints words with triple double letters from word list."""
    f = open('data/words.txt')
    for line in f:
        word = line.strip()
        if is_triple_double(word):
            print(word)


def main():
    find_triple_double()


if __name__ == "__main__":
    main()