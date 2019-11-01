from flask import Blueprint, request
from flask_restful import Resource, Api

from app import db
from app.api.models import User
from app.api.utils import UserManger

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
        data = request.get_json()

        user_manager = UserManger(_db=db, data=data)
        if user_manager.is_valid():
            user_manager.save()

            return user_manager.data, 201

        return {"message": user_manager.error}, 400


api.add_resource(UserList, '/users/')
api.add_resource(UserPingView, '/users/ping/')

