from app.models.game import Game
from flask import request, jsonify
from app import db


def index():
    return jsonify({'message': 'Game index'})
    # session = db.session()
    # try:
    #     game_list = session.query(Game).all()
    #     print (game_list)
    #     return jsonify([game.to_dict() for game in game_list])
    # except:
    #     session.rollback()
    #     return jsonify({'message': 'An error occured'}), 500

   

