from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# def create_app():
#     app = Flask(__name__)
#     CORS(app) 
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['']
#     app.register_blueprint(blueprints.game_bp)
#     db.__init__(app)
#     return app

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import blueprints

app.register_blueprint(blueprints.game_bp)

from app import routes, models, controllers, factory