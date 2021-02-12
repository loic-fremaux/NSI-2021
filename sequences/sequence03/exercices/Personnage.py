from __future__ import annotations


class Personnage:
    """
    Représente un personnage
    """

    def __init__(self, nom: str, race: str, PV: int, PA: int, inventaire):
        """
        Initialise le personnage
        :param nom: le nom
        :param race: son type
        :param PV: ses points de vie
        :param PA: ses points d'attaque
        :param inventaire: le contenu de son inventaire
        """
        self.nom = nom
        self.race = race
        self.PV = PV
        self.PA = PA
        self.inventaire = inventaire

    def __repr__(self):
        return self.nom

    def attaquer(self, cible: Personnage):
        """
        Fait perdre le nombre de points d'attaques en points de vie au personnage :param: cible
        Affiche ensuite le résultat de l'attaque et les points de vie restants de la cible
        Si le personnage meurt, son inventaire est récupéré par celui qui attaque
        :param cible: le personnage à attaquer
        """
        print(cible.nom, "a été attaqué par", self.nom, "et a perdu", self.PA, "PV")
        if cible.PV > self.PA:
            cible.PV -= self.PA
            print(cible.nom, "a désormais", cible.PV, "PV")
        else:
            cible.PV = 0
            print(cible.nom, "est mort")
            self.inventaire.append(cible.inventaire)
            cible.inventaire.clear()

    def force(self) -> int:
        """
        Renvoie la somme des points de vie et d'attaque
        :return: int
        """
        return self.PV + self.PA

    def est_plus_fort(self, cible: Personnage) -> bool:
        """
        Renvoie True si le personnage est plus fort que la cilbe, sinon renvoie False
        :param cible: Personnage à comparer
        :return: bool
        """
        return self.force() > cible.force()

    def en_vie(self) -> bool:
        """
        Renvoie True si les pv sont supérieurs à zéro, sinon false
        :return: bool
        """
        return self.PV > 0

    def print(self):
        """
        Écrit la description du personnage
        """
        print(self.nom, "est un", self.race)

    def comparaison(self, cible: Personnage) -> bool:
        """
        Renvoie True si le nombre de PV de ce personnage est supérieur à ceux de la cible renvoie False sinon
        :param cible: Personnage
        :return: bool
        """
        return self.PV > cible.PV


def force(perso: Personnage):
    return perso.PV + perso.PA


def est_plus_fort(perso1: Personnage, perso2: Personnage):
    return force(perso1) > force(perso2)


alex = Personnage("Alex", "gros chien", 100, 5, [])
jeff = Personnage("Jeff", "elf", 80, 8, [])

alex.attaquer(jeff)
jeff.attaquer(alex)

alex.PA += 2
alex.inventaire.append("os")
