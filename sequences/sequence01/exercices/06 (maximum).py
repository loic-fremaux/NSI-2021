def maximum(tab):
    """
    get the greatest number of a list
    :param tab: the list
    :return: the greatest number
    """
    high = tab[0]
    for i in range(1, len(tab)):
        if high < tab[i]:
            high = tab[i]
    return high


print(maximum([1, 6, 3, 9, 0]))
