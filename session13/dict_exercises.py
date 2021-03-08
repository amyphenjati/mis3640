# exercise 1
# 1
def histogram(s):
    """returns a dictionary of the number of each character in given string
    s: string
    """
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


h = histogram("Bookkeeper")
print(h)

# 2
def word_frequency():
    """Use function histogram to count the frequency of each
    word in your favorite song."""

    song = open("data/yellow_submarine.txt")
    d = dict()
    for line in song:
        line = line.strip()
        line = line.lower()
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""  # remove punctuation https://www.programiz.com/python-programming/examples/remove-punctuation
        no_punct = ""  # remove punctuation
        for char in line:  # remove punctuation
            if char not in punctuations:  # remove punctuation
                no_punct = no_punct + char  # remove punctuation
        words = line.split(" ")
        for word in words:
            d[word] = d.get(word, 0) + 1
    return d


print(word_frequency())


#  exercise 3
#  Global variables are declared outside any function or a global scope, and they can be used on any function in the file.
#  Local variables are inside and specifically made for that function.

#  exercise 4
# 1


def check_dict(item):
    """
    function reads words in words.txt, stores them as keys in a dictionary,
    and allows us to check whether an string is in the dictionary.
    """
    txt_file = open("data/words.txt")
    d = dict()
    for line in txt_file:
        word = line.strip()
        d[word] = word
    item = str(item)
    return item in d


print(check_dict('aba'))
print(check_dict('alskjd;fs'))

# 2


def has_duplicates(items):
    """
    function takes a list as a parameter and
    returns True if there is any object that appears more than once in the list.
    """
    items = list()
    items.sort()
    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            return True
    return False
