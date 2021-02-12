from __future__ import annotations


class Domino:
    def __init__(self, gauche: int, droite: int, posX=None, posZ=None):
        self.gauche = gauche
        self.droite = droite
        self.posX = posX
        self.posZ = posZ

    def est_double(self):
        return self.gauche == self.droite

    def est_blanc(self):
        return self.gauche == 0 and self.droite == 0

    def points(self):
        return self.gauche + self.droite

    def print(self) -> str:
        return " ----- ----- \n" \
               + "|  " + str(self.gauche) + "  |  " + str(self.droite) + "  |\n" \
               + " ----- ----- " \
            if not self.est_double() else \
            " ----- \n" \
            + "|  " + str(self.gauche) + "  |\n" \
            + " ----- \n" \
            + "|  " + str(self.gauche) + "  |\n" \
            + " ----- "

    def height(self):
        return len(self.print().split("\n"))

    def length(self):
        return len(self.print().split("\n")[0])


domino1 = Domino(3, 3)
domino2 = Domino(2, 4)

print(domino1.print())
print(domino2.print())


class JeuDomino:
    def __init__(self, nbrJoueurs: int):
        self.nbrJoueurs = nbrJoueurs
        self.game = [
            Domino(2, 3, 0, 0),
            Domino(4, 2, 0, -1),
            Domino(6, 4, 0, -2),
            Domino(4, 4, 0, 1),
            Domino(4, 6, 0, 2)
        ]
        #  self.create_game()

    def create_game(self):
        for i in range(1, 7):
            for j in range(1, 7):
                self.game.append(Domino(i, j))

    def print_board(self):
        min_x = 0
        max_x = 0
        min_z = 0
        max_z = 0
        by_index = {}
        for domino in self.game:
            if domino.posX is not None and domino.posZ is not None:
                by_index[(domino.posX, domino.posZ)] = domino
                if domino.posX < min_x:
                    min_x = domino.posX
                elif domino.posX > max_x:
                    max_x = domino.posX
                if domino.posZ < min_z:
                    min_z = domino.posZ
                elif domino.posZ > max_z:
                    max_z = domino.posZ

        result = ""
        for z in range(min_z, max_z + 1):
            result += by_index[(0, z)].print() + "\n"
        return result


jeu = JeuDomino(2)
print(jeu.print_board())
