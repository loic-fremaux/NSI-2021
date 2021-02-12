from __future__ import annotations

from sequences.sequence06.exercices.lists import Cellule


class Pile:
    current_size = 0

    def __init__(self, size=5):
        self.contenu = None
        self.size = size

    def est_vide(self):
        return self.contenu is None

    def empiler(self, elt) -> Pile:
        if self.current_size == self.size:
            raise MemoryError("La pile est pleine")
        self.current_size += 1
        c = Cellule(elt, self.contenu)
        self.contenu = c
        return self

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        else:
            self.current_size -= 1
            sommet = self.contenu.valeur
            self.contenu = self.contenu.suivante
            return sommet

    def show(self):
        Q = creer_pile_vide()
        while not est_vide(P):
            x = depiler(P)
            print(x)
            empiler(Q, x)

        while not est_vide(Q):
            x = depiler(Q)
            empiler(P, x)


def creer_pile_vide() -> Pile:
    return Pile(100)


def est_vide(P: Pile) -> bool:
    return P.est_vide()


def empiler(P: Pile, elt):
    P.empiler(elt)


def depiler(P: Pile):
    return P.depiler()


def retourner(P, i):
    Q = creer_pile_vide()
    n = 0
    while not est_vide(P) and n < i:
        n += 1
        x = depiler(P)
        empiler(Q, x)

    R = creer_pile_vide()
    while not est_vide(Q):
        empiler(R, depiler(Q))

    while not est_vide(R):
        x = depiler(R)
        empiler(P, x)


def max_pile(P, i):
    Q = creer_pile_vide()
    j = 0
    c = 1

    x = depiler(P)
    empiler(Q, x)
    max = x
    while not est_vide(P) and c < i:
        x = depiler(P)
        empiler(Q, x)
        if x > max:
            j = c
            max = x
        c += 1

    while not est_vide(Q):
        x = depiler(Q)
        empiler(P, x)

    return j


def hauteur_pile(P):
    Q = creer_pile_vide()
    n = 0
    while not est_vide(P):
        n += 1
        x = depiler(P)
        empiler(Q, x)

    while not est_vide(Q):
        x = depiler(Q)
        empiler(P, x)
    return n


def tri_crepes(P):
    h = hauteur_pile(P)
    c = h
    while c > 0:
        i = max_pile(P, c)
        retourner(P, i)
        P.show()
        print("STEP")
        retourner(P, h)
        P.show()
        print(i, c, h)

        c -= 1


P = Pile(10) \
    .empiler(7) \
    .empiler(14) \
    .empiler(12) \
    .empiler(5) \
    .empiler(8)

tri_crepes(P)

P.show()