def rech_naive(motif: str, texte: str):
    m = len(motif)
    n = len(texte)
    r = []
    for i in range(n - m + 1):
        j = 0
        while j < m and motif[j] == texte[i + j]:
            j += 1
        if j == m:
            r.append(i)
    return r


# TESTS
print(rech_naive("log", "zoologielog"))
