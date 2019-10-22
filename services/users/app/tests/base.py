from flask_testing import TestCase

from app import  db
from app.tests import app


class BaseTestCase(TestCase):

    @staticmethod
    def create_app():
        app.config.from_object('app.config.TestingConfig')

        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()