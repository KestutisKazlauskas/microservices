import sys
import unittest
from flask.cli import FlaskGroup

from app import create_app, db

# Import all models to crate tables in recreate_db command
from app.api.models import User
app = create_app()

cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs all services tests"""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    sys.exit(result)

if __name__ == '__main__':
    cli()
