from flask.cli import FlaskGroup

from app import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()

# TODO make sh file for export environment variables
# export FLASK_APP=project/__init__.py
# export FLASK_ENV=development
