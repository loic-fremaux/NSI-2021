from sequence06.exercices.piles import Pile

P1 = Pile(6)\
    .empiler(4)\
    .empiler(9)\
    .empiler(5)\
    .empiler(1)\
    .empiler(3)\
    .empiler(2)


def renverser(P: Pile) -> Pile:
    R = Pile()
    c = 0
    index = P
    while not P.est_vide():
        R.empiler(index.depiler())
        c += 1
    return R


c1 = 0
index1 = renverser(P1)
while not index1.est_vide():
    print(index1.depiler())
    c1 += 1
