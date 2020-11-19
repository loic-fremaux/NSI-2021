import math


def renverser_rec(tab: list, i: int):
    """
    Inverse l'ordre des éléments du tableau tab en utilisant la récursivité
    :param tab: list
    :param i: int le point de pivot actuel des éléments
    """
    tab_len = len(tab) - 1
    if math.ceil(tab_len / 2) - i == 0:
        return tab
    tab[i], tab[tab_len - i] = tab[tab_len - i], tab[i]
    return renverser_rec(tab, i + 1)


testTab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
renverser_rec(testTab, 0)
print(testTab)

testTab = [1, 2, 3, 4, 5, 6, 7]
renverser_rec(testTab, 0)
print(testTab)
