import multiprocessing
import time

from pong_libs import *

import socket

HOST = '127.0.0.1'
PORT = 56789

stop = False
threads = []
closeable = []


def get_json_mouse_data() -> str:
    x, y = pygame.mouse.get_pos()
    return json.dumps({
        "mouse": {
            "x": x,
            "y": y
        }
    })


def network_loop(game: PongGame):
    global stop
    sleep_rate = 1 / TICK_RATE
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(str.encode("ping"))
    closeable.append(client)
    with client:
        while True:
            data = client.recv(1024)
            if not data or stop:
                break

            msg = data.decode()
            json_data = json.loads(msg)

            game.player_server.pad.x = json_data["pad_server"]["x"]
            game.player_server.pad.y = json_data["pad_server"]["y"]

            game.player_client.pad.x = json_data["pad_client"]["x"]
            game.player_client.pad.y = json_data["pad_client"]["y"]

            game.ball.x = json_data["ball"]["x"]
            game.ball.y = json_data["ball"]["y"]

            game.player_server.score = json_data["score"]["server"]
            game.player_client.score = json_data["score"]["client"]

            client.sendall(str.encode(get_json_mouse_data()))
            time.sleep(sleep_rate)


def close():
    for t in threads:
        t.terminate()
    for c in closeable:
        c.close()
    socket.close(0)
    sys.exit()


def main():
    global stop
    game = PongGame()

    net_thread = multiprocessing.Process(target=network_loop, args=(game, ))
    net_thread.start()
    threads.append(net_thread)

    # GAME LOOP
    while True:
        if game.manage_events():
            stop = True
            break

        game.show()
        pygame.display.flip()
        CLOCK.tick(TICK_RATE)


main()
