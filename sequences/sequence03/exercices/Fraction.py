from __future__ import annotations


class Fraction:
    def __init__(self, num: float, denom: float):
        self.num = num
        self.denom = denom
        if denom == 0:
            raise ValueError("Le dénominateur ne peut pas être 0")

    def __repr__(self):
        return str(self.num) + "/" + str(self.denom)

    def __str__(self):
        return self.__repr__()

    def addition(self, other: Fraction) -> Fraction:
        self.num = self.num * other.denom + self.denom * other.num
        self.denom = self.denom * other.denom
        self.simplifier()
        return self

    def soustraction(self, other: Fraction) -> Fraction:
        self.num = self.num * other.denom - self.denom * other.num
        self.denom = self.denom * other.denom
        self.simplifier()
        return self

    def multiplication(self, other: Fraction) -> Fraction:
        self.num = self.num * other.num
        self.denom = self.denom * other.denom
        self.simplifier()
        return self

    def division(self, other: Fraction) -> Fraction:
        self.num = self.num * other.denom
        self.denom = self.denom * other.num
        self.simplifier()
        return self

    def simplifier(self):
        diviseur_commun = self.pgcd()
        self.num = self.num / diviseur_commun
        self.denom = self.denom / diviseur_commun

    def pgcd(self):
        a = self.num
        b = self.denom
        while b:
            a, b = b, a % b
        return a

    def __eq__(self, other):
        return self.num / self.denom == other.num / other.denom

    def __ne__(self, other):
        return self.num / self.denom != other.num / other.denom

    def __gt__(self, other):
        return self.num / self.denom > other.num / other.denom

    def __ge__(self, other):
        return self.num / self.denom >= other.num / other.denom

    def __lt__(self, other):
        return self.num / self.denom < other.num / other.denom

    def __le__(self, other):
        return self.num / self.denom <= other.num / other.denom

    def __add__(self, other):
        return self.addition(other)

    def __sub__(self, other):
        return self.soustraction(other)

    def __mul__(self, other):
        return self.multiplication(other)

    def __div__(self, other):
        return self.division(other)
