def codage(mot: str, decalage: int) -> str:
    """
    Permet de chiffrer une chaîne de caractères mot avec le code de césar en utilisant un décalage défini
    :param mot: str
    :param decalage: int
    :return: str
    """
    result = ""
    for c in mot:
        result += convertir(c, decalage)
    return result


def convertir(lettre: str, decalage: int) -> str:
    """
    Convertis un caractère avec le code de césar
    :param lettre: str[1]
    :param decalage: int
    :return: Le caractère déplacé de decalage éléments dans la table ASCII
    """
    c = ord(lettre)
    if 96 < c < 123:
        if c + decalage > 122:
            decalage = 97 + (c + decalage - 122) - 123
    if 64 < c < 91:
        if c + decalage > 90:
            decalage = 65 + (c + decalage - 90) - 91

    return chr(c + decalage)


print(codage('NSI', 4))
print(codage('Zoo', 4))
