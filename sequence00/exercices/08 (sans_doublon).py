def sans_doublon(tab):
    """
    Remove duplicates values of a array and return a new one
    :param tab: the array
    :return: new array without duplicates
    """
    result = []
    for elt in tab:
        i = 0
        l = len(result)
        while i < l and elt != result[i]:
            i += 1
        if i == l:
            result.append(elt)
    return result


print(sans_doublon([1, "a", 5, "a", 1, 2]))
