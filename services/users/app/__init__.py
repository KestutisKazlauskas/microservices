import os

from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# init flask and flask api
app = Flask(__name__)
api = Api(app)

# init app settings
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# database inti
db = SQLAlchemy(app)

# TODO remove to models.py
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# TODO remove to separate api user module
class UserPingView(Resource):

    @staticmethod
    def get():

        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(UserPingView, '/users/ping/')
