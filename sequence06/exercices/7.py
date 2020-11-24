from sequence06.exercices.lists import Liste, cons

L2 = cons(5, cons(2, cons(3, cons(6, cons(1, cons(7, None))))))

def longueur_list(L: list) -> int:
    c = 0