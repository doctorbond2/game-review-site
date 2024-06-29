from app.models.game import Game
from app.models.genre import Genre
from flask import request, jsonify
from app import db
from sqlalchemy.orm import joinedload

# def index():

#     session = db.session()
#     try:
#         genre_list = session.query(Genre).all()
#         return jsonify([genre.to_dict_with_games(session) for genre in genre_list])
#     except Exception as e:
#         print(f'Error: {e}')
#         session.rollback()
#         return jsonify({'message': 'An error occured'}), 500
   
def index():
    session = db.session()
    try:
        game_list = session.query(Game).all()
        return jsonify([game.to_dict(session) for game in game_list])
    except Exception as e:
        print(f'Error: {e}')
        session.rollback()
        return jsonify({'message': 'An error occured'}), 500

# def index_two():
#     session = db.session()
#     try:
#         genre_list = session.query(Genre).all()
#         return jsonify([genre.to_dict() for genre in genre_list])
#     except Exception as e:
#         print(f'Error: {e}')
#         session.rollback()
#         return jsonify({'message': 'An error occured'}), 500

