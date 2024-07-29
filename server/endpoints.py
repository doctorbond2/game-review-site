
from dotenv import load_dotenv
import os
load_dotenv('.routesenv')

class Game_ENV:
    base_url = os.getenv('GAME_BASE_URL')
    index = os.getenv('GAME_INDEX')
    post_one_game = os.getenv('GAME_POST_ONE')
    get = os.getenv('GAME_GET')
    get_one_game_by_id = os.getenv('GAME_GET_ONE_BY_ID')
    get_one_game_by_name = os.getenv('GAME_GET_ONE_BY_NAME')
    get_one_game_details = os.getenv('GAME_GET_ONE_DETAILS')

class Review_ENV:
    base_url= os.getenv('REVIEW_BASE_URL')
    post_one_review = os.getenv('REVIEW_USER_POST_ONE')

class User_ENV:
    base_url = os.getenv('USER_BASE_URL')
    auth_base_url = os.getenv('USER_AUTH_BASE_URL')
    post_login_user = os.getenv('USER_AUTH_LOGIN')
    put_update_password = os.getenv('USER_AUTH_UPDATE_PASSWORD')
