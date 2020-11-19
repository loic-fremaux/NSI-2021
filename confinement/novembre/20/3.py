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
    if 'A' <= lettre.upper() <= 'Z':
        first_index = ord('a') if lettre.islower() else ord('A')
        return chr((ord(lettre) - first_index + decalage) % 26 + first_index)
    else:
        return lettre


for i in range(-26, 0):
    print(codage('Zo poapcqvs, q\'sgh hsfawb !', i))
