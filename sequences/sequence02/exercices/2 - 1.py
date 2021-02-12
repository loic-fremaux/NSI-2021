def rech_naive(motif: str, texte: str):
    m = len(motif)
    n = len(texte)
    for i in range(n - m + 1):
        j = 0
        while j < m and motif[j] == texte[i + j]:
            j += 1
        if j == m:
            return True
    return False


# TESTS
print(rech_naive("log", "zoologie"))
print(rech_naive("logique", "zoologie"))
