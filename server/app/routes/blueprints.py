from flask import Blueprint
from endpoints import Game_ENV, Review_ENV
print(Game_ENV.base_url)
game_bp = Blueprint('games', __name__,url_prefix=Game_ENV.base_url)

user_bp = Blueprint('users', __name__)

review_bp = Blueprint('reviews', __name__, url_prefix=Review_ENV.base_url)