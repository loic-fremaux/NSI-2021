import sys
from typing import Tuple

import pygame
import pygame.freetype
import math
import json

pygame.init()
pygame.freetype.init()


# MAGICK VALUES

BLUE = pygame.Color("#00ffcc")
GRIS_CLAIR = pygame.Color("#0d8876")
GRIS = pygame.Color("#154143")
BLACK = pygame.Color("#1a1221")


TICK_RATE = 60
WIDTH, HEIGHT = 600, 800

BALL_RADIUS = 10
X_MIN, Y_MIN = 0, 0
X_MAX, Y_MAX = WIDTH, HEIGHT

MAIN_FONT = pygame.font.Font(None, 32)
TITLE_FONT = pygame.font.Font(None, 64)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()


# GAME DEFINITION
pygame.display.set_caption("Pong Game")


# CLASSES

class Ball:
    def angle_speed(self, angle):
        self.vx = self.speed * math.cos(math.radians(angle))
        self.vy = self.speed * math.sin(math.radians(angle))

    def __init__(self):
        self.x, self.y = (400, 400)
        self.speed = 5
        self.angle_speed(60)
        self.on_pad = True

    def show(self):
        pygame.draw.rect(SCREEN, BLUE,
                         (int(self.x - BALL_RADIUS), int(self.y - BALL_RADIUS), 2 * BALL_RADIUS, 2 * BALL_RADIUS), 0)

    def bounce(self, pad):
        diff = pad.x - self.x
        total_length = pad.length / 2 + BALL_RADIUS
        angle = 90 + 80 * diff / total_length
        self.angle_speed(angle)

    def move(self, pad1, pad2):
        if self.on_pad:
            self.y = pad1.y - 2 * BALL_RADIUS
            self.x = pad1.x
        else:
            self.x += self.vx
            self.y += self.vy
            if pad1.ball_collision(self) and self.vy > 0:
                self.bounce(pad1)
                self.vy = -self.vy
            if pad2.ball_collision(self) and self.vy > 0:
                self.bounce(pad2)
                self.vy = -self.vy
            if self.x + BALL_RADIUS > X_MAX:
                self.vx = -self.vx
            if self.x - BALL_RADIUS < X_MIN:
                self.vx = -self.vx
            if self.y + BALL_RADIUS > Y_MAX:
                self.on_pad = True
                # score player two
            if self.y - BALL_RADIUS < Y_MIN:
                self.vy = -self.vy
                # score player one


class Pad:
    def __init__(self):
        self.x = (X_MIN + X_MAX) / 2
        self.y = Y_MAX - BALL_RADIUS - 40
        self.length = 10 * BALL_RADIUS

    def show(self):
        pygame.draw.rect(SCREEN,
                         BLUE,
                         (int(self.x - self.length / 2), int(self.y - BALL_RADIUS), self.length, 2 * BALL_RADIUS),
                         0
                         )

    def move(self, x):
        if x - self.length >> 1 < X_MIN:
            self.x = X_MIN + self.length >> 1
        elif x + self.length >> 1 > X_MAX:
            self.x = X_MAX - self.length >> 1
        else:
            self.x = x

    def ball_collision(self, ball):
        vertical = abs(self.y - ball.y) < 2 * BALL_RADIUS
        horizontal = abs(self.x - ball.x) < self.length / 2 + BALL_RADIUS
        return vertical and horizontal


class Player:
    def __init__(self):
        self.pad = Pad()
        self.score = 0


class PongGame:
    def __init__(self):
        self.ball = Ball()
        self.player_client = Player()
        self.player_server = Player()

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.ball.on_pad:
                        self.ball.on_pad = False
                        self.ball.angle_speed(60)

    def update_board(self):
        x, y = pygame.mouse.get_pos()
        self.player_server.pad.move(x)
        self.ball.move(self.player_server.pad, self.player_client.pad)

    def show(self):
        SCREEN.fill(BLACK)
        self.ball.show()
        self.player_server.pad.show()
        self.player_client.pad.show()


# STATIC METHODS

def clear_board():
    SCREEN.fill(BLACK)


def print_text(font: pygame.font.Font, message: str, color: pygame.Color, position: Tuple):
    text = font.render(message, True, color)
    rect = text.get_rect(center=position)
    SCREEN.blit(text, rect)


def repeat(text: str, times: int) -> str:
    s = ""
    for i in range(times):
        s += text
    return s
