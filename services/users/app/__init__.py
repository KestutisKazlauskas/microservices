from flask import Flask
from flask_restful import Api, Resource

# init flask and flask api
app = Flask(__name__)
api = Api(app)

app.config.from_object('app.config.DevelopmentConfig')


# TODO remove to separate api user module
class UserPingView(Resource):

    @staticmethod
    def get():

        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(UserPingView, '/users/ping/')
