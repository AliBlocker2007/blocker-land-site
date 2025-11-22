import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this-to-a-random-secret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'booking.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
