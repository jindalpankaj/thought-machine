import os

basedir = os.path.abspath(os.path.dirname(__file__))   


class Config(object):

    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    print("My-message: Getting database URI now...")
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # for local, set DATABASE_URL = postgresql://postgres:test@localhost:5432/thought_db_psql
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    # or 'postgresql://postgres:test@localhost:5432/thought_db_psql'
    # 'sqlite:///' + os.path.join(basedir, 'thought_db_2.db?check_same_thread=False')
                              
    print("My-message: Found database URI is: ", SQLALCHEMY_DATABASE_URI)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False   
    