import os
import datetime  
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something-something-darkside'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SERVER_NAME = os.environ.get('SERVER_NAME') or '127.0.0.1:5050'
    JWT_SECRET_KEY = 'absolut!xd'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)  
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)

