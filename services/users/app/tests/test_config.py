import os
import unittest

from flask import current_app
from flask_testing import TestCase

from app.tests import app


class MainConfigTestCase(TestCase):

    config = None

    def create_app(self):
        app.config.from_object(self.config)
        return app


class TestDevelopmentConfig(MainConfigTestCase):

    config = 'app.config.DevelopmentConfig'

    def test_app_is_development(self):
        self.assertEqual(app.config['SECRET_KEY'], 'my_precious')
        self.assertNotEqual(current_app, None)
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'], os.getenv('DATABASE_URI'))


class TestTestingConfig(MainConfigTestCase):

    config = 'app.config.TestingConfig'

    def test_app_is_testing(self):
        self.assertEqual(app.config['SECRET_KEY'], 'my_precious')
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'], os.getenv('DATABASE_URI_TESTING'))


class TestProductionConfig(MainConfigTestCase):

    config = 'app.config.ProductionConfig'

    def test_app_is_testing(self):
        self.assertEqual(app.config['SECRET_KEY'], 'my_precious')
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()