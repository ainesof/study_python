import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URL = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'apps.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False