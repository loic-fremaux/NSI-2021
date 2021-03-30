import asyncio
import json
import multiprocessing
import time
from threading import Thread

import pygame.freetype
from pong_libs import *
import socket

HOST = '0.0.0.0'
PORT = 56789

connected = False


def get_json_game_data(game: PongGame) -> str:
    return json.dumps({
        "pad_server": {
            "x": game.player_server.pad.x,
            "y": game.player_server.pad.y
        },
        "pad_client": {
            "x": game.player_client.pad.x,
            "y": game.player_client.pad.y
        },
        "ball": {
            "x": game.ball.x,
            "y": game.ball.y
        },
        "score": {
            "server": game.player_server.score,
            "client": game.player_client.score
        }
    })


class NetThread:
    def __init__(self, game: PongGame):
        self.closing = False
        self.client = None
        net_thread = Thread(target=self.network_loop, args=(game,))
        net_thread.start()
        self.out_thread = net_thread

    def close(self):
        self.closing = True
        self.client.close()
        sys.exit()

    async def send_update(self, game: PongGame):
        print("send update")
        self.client.sendall(str.encode(get_json_game_data(game)))

    def network_loop(self, game: PongGame):
        global connected
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, PORT))
            server.listen()
            client, addr = server.accept()
            self.client = client
            connected = True
            with client:
                while True:
                    data = client.recv(1024)
                    if not data or self.closing:
                        self.close()
                    msg = data.decode()
                    print(msg)
                    if msg != "ping":
                        json_data = json.loads(msg)
                        game.player_client.pad.move(json_data['mouse']['x'])


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


def main():
    game = PongGame()

    # START NETWORK THREAD
    net = NetThread(game)

    # WAITING FOR SECOND PLAYER
    wait_animation(game)

    clear_board()
    print_text(MAIN_FONT, "Joueur connecté, lancement de la partie !", BLUE, (WIDTH >> 1, HEIGHT >> 1))

    # GAME LOOP
    with multiprocessing.Pool() as pool:
        while True:
            if game.manage_events():
                print_text(MAIN_FONT, "Connexion interrompue...", BLUE, (WIDTH >> 1, HEIGHT >> 1))
                net.close()
                time.sleep(3)
                sys.exit()

            game.update_board()
            game.show()
            pygame.display.flip()
            multiprocessing.Process(target=net.send_update, args=(game, ))
            CLOCK.tick(TICK_RATE)


main()
