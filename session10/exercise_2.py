def counter(word, let):
    """This function demonstrates a pattern of computation called a counter.
    The variable count is initialized to 0 and then incremented each time an a is found.
    When the loop exits, count contains the result — the total number of a letter."""
    count = 0
    for letter in word:
        if letter == let:
            count = count + 1
    return count


# test
print(counter('hi', 'i'))
