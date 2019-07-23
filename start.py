from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify

class Start(Resource):
    user1 = False
    user2 = False

    def post(self, user):
        print("POST")
        if user == '1':
            self.user1 = True
        elif user == '2':
            self.user2 = True
        return {"start": "ok"}

api.add_resource(BoardServer, '/start/<user>/')

