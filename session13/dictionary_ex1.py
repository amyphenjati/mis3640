# 1
def histogram(s):
    """returns a dictionary of the number of each character in given string
    s: string 
    """
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


h = histogram('Bookkeeper')
print(h)
