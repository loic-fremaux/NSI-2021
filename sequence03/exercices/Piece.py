from __future__ import annotations

import random


class Piece:
    etats_possibles = ["pile", "face"]

    def __init__(self, etat="", proba=0.5):
        self.etat = etat
        self.proba = proba

    def __repr__(self):
        return "La pièce est du côté " + self.etat

    def __str__(self):
        return self.__repr__()

    def lancer(self):
        self.etat = self.etats_possibles[1 if random.uniform(0, 1) > self.proba else 0]

    def lancers(self, nb) -> list:
        results = []
        for _ in range(nb):
            self.lancer()
            results.append(self.etat)
        return results

    def nb(self, n, etat) -> int:
        return self.lancers(n).count(etat)

    def nb_pile(self, n) -> int:
        return self.nb(n, "pile")

    def nb_face(self, n) -> int:
        return self.nb(n, "face")

    def jouer(self, gagnant: str) -> bool:
        self.lancer()
        return self.etat == gagnant


piece1 = Piece()
print(piece1.jouer("pile"))

piece2 = Piece("pile", 0.9)
print(piece2.jouer("pile"))
