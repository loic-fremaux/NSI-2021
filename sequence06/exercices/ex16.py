from sequence06.exercices.piles import Pile

P1 = Pile(6)\
    .empiler(4)\
    .empiler(9)\
    .empiler(5)\
    .empiler(1)\
    .empiler(3)\
    .empiler(2)


def rechercher(elt, P: Pile) -> bool:
    c = 0
    while not P.est_vide():
        if P.depiler() == elt:
            return True
        c += 1
    return False


print(rechercher(9, P1))
print(rechercher(9, P1))
print(rechercher(4, P1))
