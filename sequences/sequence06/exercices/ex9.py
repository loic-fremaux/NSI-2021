from sequences.sequence06.exercices.lists import Liste, cons

L2 = cons(5, cons(2, cons(3, cons(6, cons(1, cons(7, None))))))


def liste2tab(L: Liste) -> list:
    c = 0
    index = L
    tab = []
    while index is not None:
        tab.append(index.car())
        index = index.cdr()
        c += 1
    return tab


print(liste2tab(L2))
