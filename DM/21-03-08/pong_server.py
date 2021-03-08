import multiprocessing
import time

import pygame.freetype
from pong_libs import *
import socket

HOST = '0.0.0.0'
PORT = 56789

connected = False
stop = False
threads = []
closeable = []


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
    global stop
    sleep_rate = 1 / TICK_RATE
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        closeable.append(server)
        client, addr = server.accept()
        closeable.append(client)
        connected = True
        with client:
            while True:
                data = client.recv(1024)
                if not data or stop:
                    break
                msg = data.decode()
                if msg != "ping":
                    json_data = json.loads(msg)
                    game.player_client.pad.move(json_data['mouse']['x'])

                client.sendall(str.encode(get_json_game_data(game)))
                time.sleep(sleep_rate)


def close():
    for t in threads:
        t.terminate()
    for c in closeable:
        c.close()
    socket.close(0)
    sys.exit()


def wait_animation(game: PongGame) -> bool:
    global connected
    global stop
    t = 3
    while not connected:
        if game.manage_events():
            stop = True
            break

        pygame.display.flip()
        CLOCK.tick(2)
        clear_board()
        t += 1
        if t == 4:
            t = 0
        print_text(MAIN_FONT, "En attente du joueur 2" + repeat(".", t), BLUE, (WIDTH >> 1, HEIGHT >> 1))

    if stop:
        close()
        return True
    return False


def main():
    global stop
    game = PongGame()

    # START NETWORK THREAD
    net_thread = multiprocessing.Process(target=network_loop, args=(game, ))
    net_thread.start()
    threads.append(net_thread)

    # WAITING FOR SECOND PLAYER
    if wait_animation(game):
        return True

    clear_board()
    print_text(MAIN_FONT, "Joueur connecté, lancement de la partie !", BLUE, (WIDTH >> 1, HEIGHT >> 1))

    # GAME LOOP
    while True:
        if game.manage_events():
            stop = True
            break

        game.update_board()
        game.show()
        pygame.display.flip()
        CLOCK.tick(TICK_RATE)

    close()


main()
