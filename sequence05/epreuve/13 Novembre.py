def recherche(elt: float, tab: list) -> list:
    """
    Renvoie les indices des occurrences d'un nombre dans un tableau
    :param elt: nombre à trouver dans le tableau
    :param tab: le tableau de nombres
    :return: un tableau contenant les indices des occurrences du nombre elt dans le tableau tab
    renvoie un tableau vide si aucune occurrence n'est trouvée
    """
    return [i for i in range(len(tab)) if tab[i] == elt]


#############
#   TESTS   #
#############
print(recherche(3, [3, 2, 1, 3, 2, 1]))
print(recherche(4, [1, 2, 3]))
print(recherche(4, []))
print(recherche(4, [1, 1, 1, 1, 2, 2, 2]))
