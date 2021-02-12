def recherche4(motif, texte):
    m = len(motif)
    n = len(texte)
    i = -1
    found = False
    while i < n - m + 1 and not found:
        i += 1
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if j == m:
            found = True
    if i == n:
        return -1
    else:
        return i


#  TESTS NOT WORKING
print(recherche4("log", "zoologielog"))
print(recherche4("logique", "zoologielog"))
