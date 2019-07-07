from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

import os
import time
from threading import Thread
import random

from game import Game
from user import User


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


BOARD_SIZE = 32
GAME_PERIOD = 1 # seconds

game = Game(BOARD_SIZE)

def monitor():
    for i in range(1000):
        time.sleep(GAME_PERIOD)
        game.update_board()
        if random.randint(0, 6) == 0:
            game.add_food([random.randint(0, 31), random.randint(0, 31)])


def start_game():
    user1 = User(BOARD_SIZE)
    user2 = User(BOARD_SIZE)
    # user3 = User(10)

    game.add_user(user1)
    game.add_user(user2)
    # game.add_user(user3)

    t = Thread(target=monitor)
    t.start()



def get_board(game):
    return game.get_board()


app = Flask(__name__)
api = Api(app)

class BoardServer(Resource):
	def get(self):
		print("GET")
		#for row in game.get_board():
		#	print(row)


		#print()
		#for user in game.users:
		#	print(user.name, user.last_move)


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
	app.run(debug=True)
