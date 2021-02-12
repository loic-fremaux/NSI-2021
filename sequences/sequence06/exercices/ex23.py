from sequences.sequence06.exercices.files import File

F1 = File()\
    .enfiler(3)\
    .enfiler(1)\
    .enfiler(5)\
    .enfiler(6)\
    .enfiler(4)\
    .enfiler(2)


def copier(P: File) -> File:
    F = File()
    c = 0
    index = P
    while not P.est_vide():
        F.enfiler(index.defiler())
        c += 1
    return F

# TEST
c1 = 0
index1 = copier(F1)
while not index1.est_vide():
    print(index1.defiler())
    c1 += 1
