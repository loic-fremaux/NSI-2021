def sans_doublon_bis(tab):
    """
    Remove duplicates values of a sorted array of numbers and return a new one
    :param tab: the array
    :return: new array without duplicates
    """
    result = [tab[0]]
    for elt in tab:
        if elt != result[len(result) - 1]:
            result.append(elt)
    return result


print(sans_doublon_bis([1, 1, 2, 3, 3, 3, 4, 5]))
