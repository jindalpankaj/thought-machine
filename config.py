import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    basedir = os.path.abspath(os.path.dirname(__file__))   
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'thought_db_2.db?check_same_thread=False')

    SQLALCHEMY_TRACK_MODIFICATIONS = False