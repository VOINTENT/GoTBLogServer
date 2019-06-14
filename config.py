import os

class Config(object):
    SECRET_KEY = 'you-wil-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
