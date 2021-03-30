import asyncio
import json
import multiprocessing
from threading import Thread

from pong_libs import *

import socket

HOST = '127.0.0.1'
PORT = 56789


def get_json_mouse_data() -> str:
    x, y = pygame.mouse.get_pos()
    return json.dumps({
        "mouse": {
            "x": x
        }
    })


class NetThread:
    def __init__(self, game: PongGame):
        self.closing = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net_thread = Thread(target=self.network_loop, args=(game, self.client))
        net_thread.start()
        self.thread = net_thread

    def connect(self):
        self.client.connect((HOST, PORT))
        self.client.sendall(str.encode("ping"))

    def close(self):
        self.closing = True
        self.client.close()
        sys.exit()

    async def send_data(self):
        print("send update")
        self.client.sendall(str.encode(get_json_mouse_data()))

    def network_loop(self, game: PongGame, client):
        self.connect()
        with client:
            while True:
                data = client.recv(1024)
                if not data or self.closing:
                    self.close()

                msg = data.decode()
                print(msg)
                json_data = json.loads(msg)

                game.player_server.pad.x = json_data["pad_server"]["x"]
                game.player_server.pad.y = json_data["pad_server"]["y"]

                game.player_client.pad.x = json_data["pad_client"]["x"]
                game.player_client.pad.y = json_data["pad_client"]["y"]

                game.ball.x = json_data["ball"]["x"]
                game.ball.y = json_data["ball"]["y"]

                game.player_server.score = json_data["score"]["server"]
                game.player_client.score = json_data["score"]["client"]


def main():
    game = PongGame()

    net = NetThread(game)

    # GAME LOOP
    with multiprocessing.Pool() as pool:
        while True:
            if game.manage_events():
                net.close()
                print_text(MAIN_FONT, "Connexion interrompue...", BLUE, (WIDTH >> 1, HEIGHT >> 1))
                break

            game.show()
            pygame.display.flip()
            multiprocessing.Process(target=net.send_data)
            CLOCK.tick(TICK_RATE)


main()
