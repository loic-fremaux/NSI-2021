import math


def renverser(tab: list):
    """
    Inverse l'ordre des éléments du tableau tab
    :param tab: list
    """
    tab_len = len(tab) - 1
    for i in range(math.ceil(tab_len / 2)):
        tab[i], tab[tab_len - i] = tab[tab_len - i], tab[i]


testTab = [1, 2, 3, 4, 5, 6]
renverser(testTab)
print(testTab)

testTab = [1, 2, 3, 4, 5]
renverser(testTab)
print(testTab)
