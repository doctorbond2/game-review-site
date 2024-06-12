from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_cors import CORS
from app.routes import blueprints
from app.db import db
import os



def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(blueprints.game_bp)
    db.__init__(app)
    return app

