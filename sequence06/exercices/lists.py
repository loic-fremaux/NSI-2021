class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s


class Liste:
    def __init__(self, c: Cellule = None):
        self.contenu = c

    def is_empty(self) -> bool:
        return self.contenu is None

    def car(self) -> Cellule:
        if self.is_empty():
            raise AttributeError("La liste est vide")
        else:
            return self.contenu.valeur

    def cdr(self) -> Cellule:
        if self.is_empty():
            raise AttributeError("La liste est vide")
        else:
            return self.contenu.suivante


def cons(tete, queue):
    return Liste(Cellule(tete, queue))


nil = Liste()
