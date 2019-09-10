import sys
import unittest
from flask.cli import FlaskGroup

from app import app, db

cli = FlaskGroup(app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session_commit()

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
