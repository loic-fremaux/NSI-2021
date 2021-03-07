from threading import Thread

import pygame.freetype
from pong_libs import *
import socket

HOST = '127.0.0.1'
PORT = 56789

connected = False


def network_loop():
    global connected
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        client, addr = server.accept()
        connected = True
        with client:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                client.sendall(data)


def wait_animation(game: PongGame):
    global connected
    t = 3
    while not connected:
        game.manage_events()
        pygame.display.flip()
        CLOCK.tick(2)
        clear_board()
        t += 1
        if t == 4:
            t = 0
        print_text(MAIN_FONT, "En attente du joueur 2" + repeat(".", t), BLUE, (WIDTH >> 1, HEIGHT >> 1))

    clear_board()
    print_text(MAIN_FONT, "Joueur connecté, lancement de la partie !", BLUE, (WIDTH >> 1, HEIGHT >> 1))


def main():
    game = PongGame()

    net_thread = Thread(target=network_loop)
    net_thread.start()
    wait_animation(game)

    while True:
        game.manage_events()
        pygame.display.flip()
        CLOCK.tick(120)


main()
