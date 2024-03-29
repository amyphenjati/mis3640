import random
import string
import sys
from unicodedata import category


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="UTF8")

    # TODO: explain skip_header
    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith("*** START OF THIS PROJECT"):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    # 1. create a list for return, freq_word_list
    # 2. use for to look over the dict, hist
        # 1. get the word, freq from hist
        # 2. create the tuple this way (freq, word)
        # 3. append the tuple to freq_word_list
    # 3. sort freq_word_list
    # 4. return it
    freq_word_list = []
    for word, freq in hist.items():
        freq_word_list.append((freq, word))
    freq_word_list.sort()
    freq_word_list.reverse()
    return freq_word_list


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    dic = {}
    for key in d1:
        if key not in d2:
            dic[key] = None
    return dic


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)
    return random.choice(t)


def main():
    hist = process_file("data/alice.txt", skip_header=True)
    print(hist)
    print("Total number of words:", total_words(hist))
    print("Number of different words:", different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print("The most common words are:")
    for freq, word in t[0:20]:
        print(word, "\t", freq)

    words = process_file('data/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == "__main__":
    main()
