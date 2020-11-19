def supprimer(tab: list, elt) -> list:
    """
    Prend une liste d'éléments tab et renvoie une nouvelle liste qui ne contient pas elt
    :param tab: list
    :param elt: object
    :return: list
    """
    result = []
    for i in range(len(tab)):
        if not tab[i] == elt:
            result.append(tab[i])
    return result


testTab = [1, 2, 1, 2, 3, 1, 2, 3, 4]
print(supprimer(testTab, 2))
