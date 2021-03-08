#  exercise 2
# 1. Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
# Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies.


def most_frequent(string):
    """This function takes a string and prints the letter in order of frequency"""
    string = string.replace(" ", "")  # find spaces of strings and replace with no space
    print(string)
    count = {}  #  create dictionary
    for letter in string:  # for each letter in string
        count[letter] = count.get(letter, 0) + 1
    finalcount = []
    for letter, count in count.items():
        finalcount += [(count, letter)]
    finalcount.sort(reverse=True)
    for count, letter in finalcount:
        print(letter, count)


# 2. Write a program that reads a word list from a file and prints all the sets of words that are anagrams.
def anagram_finder():
    """
    reads a word list from a file and prints all the sets of words that are anagrams.
    """
    words = open("data/tuples_anagram.txt")
    d = dict()
    for word in words:
        key = "".join(sorted(word))
        # print(key)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    return d


# 3. Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.


def anagrams_descending():
    """
    reads a word list from a file and prints all the sets of words that are anagrams
    and prints the longest list of anagrams first.
    """
    words = open("data/tuples_anagram.txt")
    d = dict()
    for word in words:
        key = "".join(sorted(word))
        # print(key)
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    print(sorted(d.items(), key=len))


def main():
    s = "this class is so much fun i love it"
    most_frequent(s)
    anagram_finder()
    anagrams_descending()


if __name__ == "__main__":
    main()
