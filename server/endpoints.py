
from dotenv import load_dotenv
import os
load_dotenv('.routesenv')

class Game_ENV:
    base_url = os.getenv('GAME_BASE_URL')
    index = os.getenv('GAME_INDEX')
    post_one_game = os.getenv('GAME_POST_ONE')
    get = os.getenv('GAME_GET')