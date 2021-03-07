import pygame.freetype
from pong_libs import *

pygame.init()

pygame.freetype.init()
main_font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 64)

score = 0
player_health = 3
nb_briques = 0
TrueLBriques = []
won = False

game = PongGame()

while True:
    if nb_briques == score:
        won = True
        player_health += 1
    game.gestion_evenements()
    game.mise_a_jour()
    game.affichage()
    pygame.display.flip()  # envoi l'image a la carte graphique
    CLOCK.tick(120)  # set a 120 fps


pygame.quit()