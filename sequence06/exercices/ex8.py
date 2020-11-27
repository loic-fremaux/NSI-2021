from sequence06.exercices.lists import Liste, cons
from sequence06.exercices.ex7 import longueur_list

L2 = cons(5, cons(2, cons(3, cons(6, cons(1, cons(7, None))))))


def access(i: int, L: Liste):
    if i < 0 or i > longueur_list(L):
        raise AttributeError("Index out of list range")
    c = 0
    index = L
    while c < i:
        index = index.cdr()
        c += 1
    return index.car()


print(access(0, L2))
print(access(5, L2))
print(access(8, L2))
