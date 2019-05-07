from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

import os
import time
from threading import Thread
import random

from game import Game
from user import User

BOARD_SIZE = 64
GAME_PERIOD = 1 # seconds

game = Game(BOARD_SIZE)

def monitor():
    for i in range(1000):
        time.sleep(GAME_PERIOD)
        game.update_board()

        if random.randint(0, 3) == 0:
            game.add_food([random.randint(0, 9), random.randint(0, 9)])


def start_game():
    user1 = User(BOARD_SIZE)
    # user2 = User(10)
    # user3 = User(10)

    game.add_user(user1)
    # game.add_user(user2)
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


		return {"borad":
			game.get_board()
		}

	def post(self):
		print("POST")
		game.update_board()
		return


api.add_resource(BoardServer, '/get_board')

if __name__ == '__main__':
	start_game()
	app.run(debug=True)