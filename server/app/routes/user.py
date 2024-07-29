import app
from app import db
from flask import jsonify, request, Blueprint
from .. import Users
from ..controllers.user import add_user, login_user
from blueprints import user_bp
user_bp.route("/add", methods=["POST"])(add_user)
user_bp.route('/login', methods=["POST"])(login_user)
user_bp.route('/friends/add',methods=["POST"](add_friend))
user_bp.route("/update/password", methods=["PUT"](update_password))


