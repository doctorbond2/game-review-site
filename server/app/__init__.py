from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import blueprints

app.register_blueprint(blueprints.game_bp)

from app import routes, models, controllers, factory