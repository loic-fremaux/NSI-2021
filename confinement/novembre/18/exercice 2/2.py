def supprimer_rec(tab: list, elt, i: int, n_tab: list) -> list:
    """
    Prend une liste d'éléments tab et renvoie une nouvelle liste qui ne contient pas elt
    :param tab: list
    :param elt: object
    :param i: int index actuel
    :param n_tab: nouvelle liste
    :return: list
    """
    if i == len(tab):
        return n_tab
    if not tab[i] == elt:
        n_tab.append(tab[i])
    return supprimer_rec(tab, elt, i + 1, n_tab)


testTab = [1, 2, 1, 2, 3, 1, 2, 3, 4]
print(supprimer_rec(testTab, 2, 0, []))
