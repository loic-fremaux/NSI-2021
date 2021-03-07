import pygame
import pygame.freetype
import math


# MAGICK VALUES


BLEU = pygame.Color("#00ffcc")
GRIS_CLAIR = pygame.Color("#0d8876")
GRIS = pygame.Color("#154143")
NOIR = pygame.Color("#1a1221")

WIDTH, HEIGHT = 800, 600

BALL_RADIUS = 10
X_MIN, Y_MIN = 0, 0
X_MAX, Y_MAX = WIDTH, HEIGHT


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()


# GAME DEFINITION
pygame.display.set_caption("Pong Game")


# CLASSES


class Ball:
    def vitesse_par_angle(self, angle):
        self.vx = self.vitesse * math.cos(math.radians(angle))
        self.vy = self.vitesse * math.sin(math.radians(angle))

    def __init__(self):
        self.x, self.y = (400, 400)
        self.vitesse = 5  # vitesse initiale
        self.vitesse_par_angle(60)  # vecteur vitesse
        self.sur_raquette = True

    def afficher(self):
        pygame.draw.rect(SCREEN, BLEU,
                         (int(self.x - BALL_RADIUS), int(self.y - BALL_RADIUS), 2 * BALL_RADIUS, 2 * BALL_RADIUS), 0)

    def rebond_raquette(self, raquette):
        diff = raquette.x - self.x
        longueur_totale = raquette.longueur / 2 + BALL_RADIUS
        angle = 90 + 80 * diff / longueur_totale
        self.vitesse_par_angle(angle)

    def deplacer(self, raquette):
        global player_health
        if self.sur_raquette:
            self.y = raquette.y - 2 * BALL_RADIUS
            self.x = raquette.x
        else:
            self.x += self.vx
            self.y += self.vy
            if raquette.collision_balle(self) and self.vy > 0:
                self.rebond_raquette(raquette)
                self.vy = -self.vy
            if self.x + BALL_RADIUS > X_MAX:
                self.vx = -self.vx
            if self.x - BALL_RADIUS < X_MIN:
                self.vx = -self.vx
            if self.y + BALL_RADIUS > Y_MAX:
                self.sur_raquette = True
                player_health -= 1
            if self.y - BALL_RADIUS < Y_MIN:
                self.vy = -self.vy


class Pad:
    def __init__(self):
        self.x = (X_MIN + X_MAX) / 2
        self.y = Y_MAX - BALL_RADIUS - 40
        self.longueur = 10 * BALL_RADIUS

    def show(self, x):
        pygame.draw.rect(SCREEN,
                         BLEU,
                         (int(self.x - self.longueur / 2), int(self.y - BALL_RADIUS), self.longueur, 2 * BALL_RADIUS),
                         0
                         )

    def move(self, x):
        if x - self.longueur / 2 < X_MIN:
            self.x = X_MIN + self.longueur / 2
        elif x + self.longueur / 2 > X_MAX:
            self.x = X_MAX - self.longueur / 2
        else:
            self.x = x

    def collision_balle(self, balle):
        vertical = abs(self.y - balle.y) < 2 * BALL_RADIUS
        horizontal = abs(self.x - balle.x) < self.longueur / 2 + BALL_RADIUS
        return vertical and horizontal


class PongGame:
    def __init__(self):
        self.balle = Ball()
        self.raquette = Pad()
        self.brique = TrueLBriques

    def gestion_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.balle.sur_raquette:
                        self.balle.sur_raquette = False
                        self.balle.vitesse_par_angle(60)

    def mise_a_jour(self):
        x, y = pygame.mouse.get_pos()
        self.balle.deplacer(self.raquette)
        for i in range(len(TrueLBriques)):
            for j in range(len(TrueLBriques[0])):
                if self.brique[i][j].en_vie():
                    self.brique[i][j].collision_balle(self.balle)
        self.raquette.move(x)

    def affichage(self):
        if player_health > 0:
            if won:
                SCREEN.fill(NOIR)
                youWinTexte = title_font.render("YOU WIN", 1, BLEU)
                textRectTitle = youWinTexte.get_rect(center=(int(X_MAX / 2), int(Y_MAX / 2)))
                SCREEN.blit(youWinTexte, textRectTitle)
                scoreTexte = main_font.render("Score : " + str(score), 1, GRIS)
                textRectScore = scoreTexte.get_rect(center=(int(X_MAX / 2), int(Y_MAX / 2) + 100))
                SCREEN.blit(scoreTexte, textRectScore)
            else:
                SCREEN.fill(NOIR)  # on efface l'écran
                self.balle.afficher()
                self.raquette.show(self.raquette.x)
                for k in range(len(TrueLBriques)):
                    for l in range(len(TrueLBriques[0])):
                        if self.brique[k][l].en_vie():
                            self.brique[k][l].show()
                scoreTexte = main_font.render("Score : " + str(score), 1, GRIS)
                SCREEN.blit(scoreTexte, (0, Y_MAX - BRICK_WIDTH))
                vieTexte = main_font.render("Vie joueur : " + str(player_health), 1, GRIS)
                SCREEN.blit(vieTexte, (0, Y_MAX - (BRICK_WIDTH * 2)))
        else:
            SCREEN.fill(NOIR)
            gameOverTexte = title_font.render("GAME OVER", 1, BLEU)
            textRectTitle = gameOverTexte.get_rect(center=(int(X_MAX / 2), int(Y_MAX / 2)))
            SCREEN.blit(gameOverTexte, textRectTitle)
            scoreTexte = main_font.render("Score : " + str(score), 1, GRIS)
            textRectScore = scoreTexte.get_rect(center=(int(X_MAX / 2), int(Y_MAX / 2) + 100))
            SCREEN.blit(scoreTexte, textRectScore)