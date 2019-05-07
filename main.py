
import os
import time
from threading import Thread
import random

from game import Game
from user import User




def monitor():
    for i in range(30):
        game.print_board()
        time.sleep(2)
        os.system('clear')
        game.update_board()

        if random.randint(0, 3) == 0:
            game.add_food([random.randint(0, 9), random.randint(0, 9)])


def start_game():
    game = Game()

    user1 = User(10)
    user2 = User(10)
    user3 = User(10)

    game.add_user(user1)
    game.add_user(user2)
    game.add_user(user3)

    game.add_food([9, 9])


def get_board():
    return game.get_board()


# t = Thread(target=monitor)
# t.start()

# while True:
#     inp = input()
#     if inp == 'u':
#         user1.last_move = 2
#     elif inp == 'r':
#         user1.last_move = 1
#     elif inp == 'd':
#         user1.last_move = 0
#     elif inp == 'l':
#         user1.last_move = 3
