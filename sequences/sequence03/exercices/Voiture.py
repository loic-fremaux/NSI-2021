from __future__ import annotations


class Voiture:
    def __init__(self, modele: str, age: int, valeur: float):
        self.modele = modele
        self.age = age
        self.valeur = valeur

    def __repr__(self):
        return "Cette voiture est une " + str(self.modele) + ". " \
               + "Elle a " + str(self.age) + " et vaut " + str(self.valeur) + " Euros."

    def comparer(self, comp: Voiture) -> bool:
        return self.valeur > comp.valeur

    def birthday(self):
        self.age += 1
        if self.age == 1:
            self.valeur *= .8
        elif self.age == 2:
            self.valeur *= .85
        elif self.age < 7:
            self.valeur *= .9
        else:
            self.valeur *= .95

    def revendre(self) -> str:
        while self.valeur >= 10_000:
            self.birthday()
        return "Il faudrait revendre la voiture après " + str(self.age) + " ans."


voiture = Voiture("Tesla de fou", 0, 45000)
print(voiture.__str__())
print(voiture.revendre())
