a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def ordre(first: str, second: str):
    """
    check if the first word is before the second one in the alphabet
    :param first: the first word
    :param second: the second word
    :return: True if the first word is before the second one in the alphabet or else False
    """
    i = 0
    n = len(first)
    first = first.lower()
    second = second.lower()
    while i < n:
        iA = a.index(first[i])
        iB = a.index(second[i])
        if iA < iB:
            return True
        elif iA > iB:
            return False
        else:
            i += 1
    return n <= len(second)


print(ordre("abc", "bcd"))
print(ordre("bcd", "abc"))
print(ordre("abc", "abc"))
print(ordre("abc", "abcd"))
