def recherche3(motif, texte):
    m = len(motif)
    n = len(texte)
    r = []
    for i in range(n - m + 1):
        if texte[i:i + m] == motif:
            r.append(i)
    return r


# TESTS
print(recherche3("log", "zoologielog"))
