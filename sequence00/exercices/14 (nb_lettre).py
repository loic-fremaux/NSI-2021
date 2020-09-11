def nb_lettre(lettre, mot):
    """
    get the number of occurrences of a given letter in a string
    :param lettre: letter to find
    :param mot: the string
    :return: the number of occurrences of a given letter in a string
    """
    result = 0
    for c in mot:
        if c == lettre:
            result += 1
    return result


print(nb_lettre("n", "ananas"))
print(nb_lettre("a", "ananas"))
