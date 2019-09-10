import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_TESTING')


class ProductionConfig(BaseConfig):
    pass
