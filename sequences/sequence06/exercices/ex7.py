from sequences.sequence06.exercices.lists import Liste, cons

L2 = cons(5, cons(2, cons(3, cons(6, cons(1, cons(7, None))))))


def longueur_list(L: Liste) -> int:
    c = 0
    index = L
    while index is not None:
        index = index.cdr()
        c += 1
    return c
