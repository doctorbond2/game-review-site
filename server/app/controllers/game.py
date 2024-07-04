from app.models.game import Game
from app.models.genre import Genre
from flask import request, jsonify
from app import db
from sqlalchemy.orm import joinedload

   
def index():
    session = db.session()
    try:
        game_list = session.query(Game).all()
        return jsonify([game.to_dict(session) for game in game_list])
    except Exception as e:
        print(f'Error: {e}')
        session.rollback()
        return jsonify({'message': 'An error occured'}), 500

def fetch_one_game(id):
    session = db.session()
    try:
        game = session.query(Game).filter(Game.id == id).one_or_none()
        if game is not None:
            return jsonify(game.to_dict(session))
        else:
            return jsonify({'message': 'Game not found'}), 404
    except Exception as e:
        print(f'Error: {e}')
        session.rollback()
        return jsonify({'message': 'An error occurred'}), 500