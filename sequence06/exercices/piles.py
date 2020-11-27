from __future__ import annotations

from sequence06.exercices.lists import Cellule


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
