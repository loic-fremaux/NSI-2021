def inverse(tab):
    """
    inverts the position of each item in a given array
    :param tab: the array
    :return: the array with inverted indexes
    """
    l = len(tab) - 1
    for i in range(len(tab) // 2):
        tab[i], tab[l - i] = tab[l - i], tab[i]
    return tab


print(inverse([1, 2, 3, 4, 5]))
print(inverse([1, 2, 3, 4, 5, 6]))
