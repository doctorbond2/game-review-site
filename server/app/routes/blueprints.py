from flask import Blueprint
from app.routes.endpoints import Game_ENV
print(Game_ENV.base_url)
game_bp = Blueprint('games', __name__,url_prefix=Game_ENV.base_url)

user_bp = Blueprint('users', __name__)