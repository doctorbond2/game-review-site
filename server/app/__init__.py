from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_cors import CORS
import os

  

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app