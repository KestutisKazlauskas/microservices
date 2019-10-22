import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# database inti
db = SQLAlchemy()

def create_app(script_info=None):

    # App initiation
    app = Flask(__name__)

    # Set configs from file
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # app extension setup
    db.init_app(app)

    # register blueprints of the app
    from app.api import user_blueprint
    app.register_blueprint(user_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
