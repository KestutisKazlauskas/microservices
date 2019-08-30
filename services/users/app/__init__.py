from flask import Flask
from flask_restful import Api

# init flask and flask api
app = Flask(__name__)
api = Api(app)