from sequences.sequence06.exercices.piles import Pile

P1 = Pile(6)\
    .empiler(4)\
    .empiler(9)\
    .empiler(5)\
    .empiler(1)\
    .empiler(3)\
    .empiler(2)

print(P1.depiler())

print(P1.depiler())

P1.depiler()
P1.depiler()

print(P1.depiler())
