from sequence06.exercices.piles import Pile

P1 = Pile(6)\
    .empiler(4)\
    .empiler(9)\
    .empiler(5)\
    .empiler(1)\
    .empiler(3)\
    .empiler(2)


def longueur_pile(P: Pile) -> int:
    c = 0
    index = P
    while not P.est_vide():
        index.depiler()
        c += 1
    return c


print(longueur_pile(P1))
