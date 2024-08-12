import app
from app import db
from flask import jsonify, request, Blueprint
from .. import Users
from ..controllers.user import add_user, login_user
from blueprints import user_bp as user
from endpoints import User_ENV as path
user.route("/add", methods=["POST"])(add_user)
user.route(path.post_login_user, methods=["POST"])(login_user)
user.route('/friends/add',methods=["POST"](add_friend))
user.route("/update/password", methods=["PUT"](update_password))
user.route("/")

