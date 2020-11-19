def echanger(tab: list, i: int, j: int):
    """
    Échange les valeurs i et j dans le tableau tab
    :param tab: list
    :param i: int
    :param j: int
    :exception IndexError: si les indices sont inférieurs à 0 ou supérieurs à la longueur du tableau
    """
    tab_len = len(tab) - 1
    if i < 0 or i > tab_len or j < 0 or j > tab_len:
        raise IndexError("Les indices doivent être compris entre 0 et " + str(tab_len))
    tab[i], tab[j] = tab[j], tab[i]


testTab = [1, 2, 3]
echanger(testTab, 0, 2)
print(testTab)

testTab = [1, 2, 3]
echanger(testTab, 0, 3)
print(testTab)
