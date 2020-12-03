from sequence06.exercices.files import File

F1 = File()\
    .enfiler(3)\
    .enfiler(1)\
    .enfiler(5)\
    .enfiler(6)\
    .enfiler(4)\
    .enfiler(2)


def longueur_file(F: File) -> int:
    c = 0
    index = F
    while not F.est_vide():
        index.defiler()
        c += 1
    return c


print(longueur_file(F1))
