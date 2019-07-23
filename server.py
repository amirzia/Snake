from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

import os
import time
from threading import Thread
import random

from game import Game
from user import User
from start import Start

user1 = None
user2 = None

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


BOARD_SIZE = 32
GAME_PERIOD = 1 # seconds

game = Game(BOARD_SIZE)
# stop_threads = False

def monitor():
    for i in range(1000 * 1000):
        time.sleep(GAME_PERIOD)
        if game.update_board() != 0:
            reset()
            continue
        if random.randint(0, 6) == 0:
            game.add_food([random.randint(0, 31), random.randint(0, 31)])
        if random.randint(0, 8) == 0:
            game.add_obstacle([random.randint(0, 31), random.randint(0, 31)])


def reset():
	print("reseting")
	global user1, user2, game
	del user1
	del user2
	User.num = 1
	time.sleep(4)

	time.sleep(GAME_PERIOD)
	user1 = User(BOARD_SIZE)
	#user2 = User(BOARD_SIZE)

	game = Game(BOARD_SIZE)
	game.add_user(user1)
	#game.add_user(user2)


def start_game():
    user1 = User(BOARD_SIZE)
    #user2 = User(BOARD_SIZE)
    # user3 = User(10)

    game.add_user(user1)
    game.add_user(user2)
    # game.add_user(user3)
    while Start.user1 == True and Start.user2 == True:
         sleep(5)
    t = Thread(target=monitor)
    t.start()



def get_board(game):
    return game.get_board()


app = Flask(__name__)
api = Api(app)


class BoardServer(Resource):
	def get(self):
		print("GET")
		return {"board": game.get_board(), "scores": game.get_scores(), "lost": game.lost}

	def post(self, user, dir):
		print("POST")

		user = game.users[int(user) - 1]
		if dir == 'up':
			user.last_move = UP
		elif dir == 'down':
			user.last_move = DOWN
		elif dir == 'right':
			user.last_move = RIGHT
		elif dir == 'left':
			user.last_move = LEFT
		game.update_board()
		return


api.add_resource(BoardServer, '/get_board', '/move/<user>/<dir>')

if __name__ == '__main__':
	start_game()
	app.run('0.0.0.0', debug=False)
