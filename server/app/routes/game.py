from app.controllers import game as controller
from flask import request
from app.routes.blueprints import game_bp as game
from endpoints import Game_ENV as path

print(path.index)
@game.route(path.index, methods=['GET'])
def index():
    return controller.index()

@game.route(
    f'{path.get}/<int:game_id>', methods=['GET'])
def fetch_one_game(game_id):
    return controller.fetch_one_game(game_id)
