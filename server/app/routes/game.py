from app.controllers import game as controller
from flask import request
from app.routes.blueprints import game_bp as game
from app.routes.endpoints import Game_ENV as path

print(path.index)
game.route(path.index, methods=['GET'])(controller.index)
