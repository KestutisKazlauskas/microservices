from flask import Blueprint
from flask_restful import Resource, Api

user_blueprint = Blueprint('users', __name__)
api = Api(user_blueprint)

class UserPingView(Resource):

    @staticmethod
    def get():

        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(UserPingView, '/users/ping/')

