def pseudo_aleatoire_suivant(n: int) -> int:
    n **= 2
    sn = str(n)
    while len(sn) < 20:
        sn = "0" + sn
    return int(sn[6:16])


def pseudo_aleatoire(n: int, g: int) -> int:
    c = 0
    while c < n + 1:
        c += 1
        g = pseudo_aleatoire_suivant(g)

    return g / 10 ** 10


print(pseudo_aleatoire(100, 1234567890))
