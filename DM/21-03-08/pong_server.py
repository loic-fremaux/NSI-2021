import pygame.freetype
from pong_libs import *
import socket

HOST = '127.0.0.1'
PORT = 56789




def main():


    print("in main")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("bind")
        s.bind((HOST, PORT))
        print("listening")
        s.listen()
        print("init network")
        conn, addr = s.accept()
        print("accepted")
        with conn:
            print('connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    # while True:
    #     if nb_briques == score:
    #         won = True
    #         player_health += 1
    #     game.manage_events()
    #     game.update_board()
    #     game.show()
    #     pygame.display.flip()
    #     CLOCK.tick(120)

    # pygame.quit()


main()
