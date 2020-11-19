def echanger(tab: list, i: int, j: int):
    """
    Échange les valeurs i et j dans le tableau tab
    :param tab: list
    :param i: int
    :param j: int
    """
    tab[i], tab[j] = tab[j], tab[i]


testTab = [1, 2, 3]
echanger(testTab, 0, 2)
print(testTab)
