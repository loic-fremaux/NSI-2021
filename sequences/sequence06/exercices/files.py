from __future__ import annotations

from sequences.sequence06.exercices.lists import Cellule


class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def enfiler(self, elt) -> File:
        c = Cellule(elt, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

        return self

    def defiler(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v
