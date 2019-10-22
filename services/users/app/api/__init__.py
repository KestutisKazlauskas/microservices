from flask import Blueprint, request
from flask_restful import Resource, Api

from app import db
from app.api.models import User

user_blueprint = Blueprint('users', __name__)
api = Api(user_blueprint)

class UserPingView(Resource):

    @staticmethod
    def get():

        return {
            'status': 'success',
            'message': 'pong!'
        }

class UserList(Resource):

    @staticmethod
    def post():
        # TODO make validation and serialization
        data = request.get_json()
        user = User(email=data.get('email'), username=data.get('username'))
        db.session.add(user)
        db.session.commit()

        return {'username': user.username, 'email': user.email}, 201


api.add_resource(UserList, '/users/')
api.add_resource(UserPingView, '/users/ping/')

