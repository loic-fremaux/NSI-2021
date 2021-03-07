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


def network_loop(game: PongGame):
    global connected
    sleep_rate = 1 / TICK_RATE
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
                msg = data.decode()
                if msg != "ping":
                    json_data = json.loads(msg)
                    game.player_client.pad.move(json_data['mouse']['x'])

                client.sendall(str.encode(get_json_game_data(game)))
                time.sleep(sleep_rate)


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
    net_thread = Thread(target=network_loop, args=(game, ))
    net_thread.start()

    # WAITING FOR SECOND PLAYER
    wait_animation(game)

    clear_board()
    print_text(MAIN_FONT, "Joueur connecté, lancement de la partie !", BLUE, (WIDTH >> 1, HEIGHT >> 1))

    # GAME LOOP
    while True:
        game.manage_events()
        game.update_board()
        game.show()
        pygame.display.flip()
        CLOCK.tick(TICK_RATE)


main()
