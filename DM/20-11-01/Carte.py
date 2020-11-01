from __future__ import annotations

import random
from enum import Enum


class Color(Enum):
    """
    Cette class représente les différentes couleurs possibles d'un jeu de cartes
    """
    TREFLE = "Trèfle",
    PIC = "Pic",
    COEUR = "Coeur",
    CARREAU = "Carreau",


class Figure(Enum):
    """
    Cette class représente les différentes figures possibles d'un jeu de cartes
    """

    @staticmethod
    def from_id(id) -> Figure:
        """
        Permet de récupérer une Figure à partir de la valeur de la carte
        :param id: valeur de la carte
        :return: Figure
        """
        for name, member in Figure.__members__.items():
            if member.value[1] == id:
                return member
        return Figure.NONE

    AS = "As", 1, 13
    ROI = "Roi", 13, 12
    DAME = "Dame", 12, 11
    VALET = "Valet", 11, 10
    NONE = "Aucune", -1, -1


class Carte:
    """
    Cette class représente une Carte
    """

    def __init__(self, value: int, color: Color):
        """
        Initialise une carte
        :param value: la valeur de la carte: un entier compris entre 1 et 13 (inclus)
        :param color: la couleur de la carte: une Color
        """
        if value > 13 or value < 1:
            raise ValueError("La valeur de la carte doit être comprise entre 1 et 13 (inclus)")
        self.value = value
        self.color = color
        self.figure = Figure.from_id(value)

    def power(self) -> int:
        """
        Renvoie la puissance de la carte (utilisé pour les comparaisons)
        :return: int
        """
        return self.value - 1 if self.figure.value[2] == -1 else self.figure.value[2]

    def __repr__(self) -> str:
        """
        Représente la carte sous forme de chaîne de caractères
        :return: une représentation de la carte
        """
        return str(self.figure.value[0] if Figure.from_id(self.value) != Figure.NONE else self.value) \
               + " de " + self.color.value[0] + " [Power: " + str(self.power()) + "]"

    def __str__(self) -> str:
        """
        Représente la carte sous forme de chaîne de caractères
        :return: une représentation de la carte
        """
        return self.__repr__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Carte):
            return o.value == self.value
        return False

    def __gt__(self, other) -> bool:
        """
        Compare cette carte à une autre en fonction de sa valeur
        :param o: la carte à comparer
        :return: True si cette carte est plus forte que l'autre
        """
        return self.power() > other.power()

    def __ge__(self, other) -> bool:
        """
        Compare cette carte à une autre en fonction de sa valeur
        :param o: la carte à comparer
        :return: True si cette carte est plus forte ou égale à l'autre
        """
        return self.power() >= other.power()

    def __lt__(self, other) -> bool:
        """
        Compare cette carte à une autre en fonction de sa valeur
        :param o: la carte à comparer
        :return: True si cette carte est moins forte que l'autre
        """
        return self.power() < other.power()

    def __le__(self, other) -> bool:
        """
        Compare cette carte à une autre en fonction de sa valeur
        :param o: la carte à comparer
        :return: True si cette carte est aussi ou moins forte que l'autre
        """
        return self.power() <= other.power()


class PaquetDeCartes:
    """
    Cette class représente un paquet de cartes
    """

    def __init__(self, size: int, cards: list | Carte = []):
        self.size = size
        self.cards = cards
        if len(self.cards) == 0:
            self.create()

    def create(self):
        """
        Génère le paquet de cartes en fonction de la taille du paquet
        """
        self.cards.clear()
        max = (self.size - (self.size % len(Color.__members__.items()))) // 4
        for name, member in Color.__members__.items():
            for num in range(1, max + 1):
                self.cards.append(Carte(num, member))

    def shuffle(self):
        """
        Mélange le paquet de cartes
        """
        random.shuffle(self.cards)

    def choice(self, n) -> list | Carte:
        """
        Prend en paramètre un nombre entier et renvoie ce nombre de cartes aléatoires
        :param n: le nombre de cartes à renvoyer
        :return: une liste de Carte
        """
        return [random.choice(self.cards) for _ in range(n)]

    def pop(self) -> Carte:
        """
        Renvoie la première carte du paquet et la retire de la liste
        :return: Carte
        """
        return None if len(self.cards) == 0 else self.cards.pop()


###############
#    TESTS    #
###############


size = 52
half = size // 2
paquet = PaquetDeCartes(size)
paquet.shuffle()

p1 = PaquetDeCartes(half, paquet.cards[:half])
p2 = PaquetDeCartes(half, paquet.cards[half:])

co = 0
c = []
win = False

while len(p1.cards) > 0 and len(p2.cards) > 0 and co < 10000 and not win:
    co += 1
    c1 = p1.pop()
    c2 = p2.pop()

    if c1 is None or c2 is None:
        break

    while c1.__eq__(c2):
        print("Les deux joueurs ont la même carte, nouvelle tentative")
        c.append(c1)
        c.append(c2)

        t1 = p1.pop()
        t2 = p2.pop()

        if t1 is None:
            win = True
        else:
            c.append(t1)

        if t2 is None:
            win = True
        else:
            c.append(t2)

        c1 = p1.pop()
        c2 = p2.pop()
        if c1 is None or c2 is None:
            win = True
        if win:
            break

    if win:
        break

    if c1.__gt__(c2):
        c.append(c2)
        c.append(c1)
        for i in range(len(c)):
            card = c.pop()
            if card is not None:
                p2.cards.append(card)
        print("Le joueur 1 gagne ce tour")
    else:
        c.append(c2)
        c.append(c1)
        for i in range(len(c)):
            card = c.pop()
            if card is not None:
                p1.cards.append(card)
        print("Le joueur 2 gagne ce tour")

    print("Fin du tour, le joueur 1 a", len(p1.cards), "cartes et le joueur 2 a", len(p2.cards), "cartes")


print("Partie terminée, joueur " + ("1" if len(p1.cards) == 0 else "2") + " remporte la partie")
