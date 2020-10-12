def table_boyer_moore(motif):
    d = [{} for i in range(len(motif))]
    for j in range(len(motif)):
        for k in range(j):
            d[j][motif[k]] = k
    return d


def decalage(d, j, chr):
    if chr in d[j]:
        return j - d[j][chr]
    else:
        return j + 1


def rech_boyer_moore(motif, texte):
    d = table_boyer_moore(motif)
    i = 0
    reponse = []
    while i <= len(texte) - len(motif):
        k = 0
        j = len(motif) - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j -= 1
        if j != -1:
            k = decalage(d, j, texte[i + j])
        if k == 0:
            reponse.append(i)
            k = 1
        i += k
    return reponse


print(rech_boyer_moore("TGAC", "AATCGAACTGACAA"))

print(table_boyer_moore("banane"))
