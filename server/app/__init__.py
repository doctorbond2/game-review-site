from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
jwt = JWTManager(app)

from app.routes import blueprints

app.register_blueprint(blueprints.game_bp)
app.register_blueprint(blueprints.review_bp)
CORS(app)
from app import routes, models, controllers, factory