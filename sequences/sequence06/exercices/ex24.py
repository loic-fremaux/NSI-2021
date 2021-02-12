from sequences.sequence06.exercices.files import File

F1 = File()\
    .enfiler(3)\
    .enfiler(1)\
    .enfiler(5)\
    .enfiler(6)\
    .enfiler(4)\
    .enfiler(2)


def rechercher(elt, P: File) -> bool:
    c = 0
    while not P.est_vide():
        if P.defiler() == elt:
            return True
        c += 1
    return False


print(rechercher(5, F1))
print(rechercher(2, F1))
print(rechercher(5, F1))
