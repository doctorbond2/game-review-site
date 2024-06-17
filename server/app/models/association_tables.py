from app import db
import sqlalchemy as sa

# Association table for the many-to-many relationship between Game and Genre
game_genre_association = db.Table('game_genre',
    db.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), primary_key=True),
    db.Column('genre_id', sa.Integer, sa.ForeignKey('genres.id'), primary_key=True)
)
game_system_association = db.Table('game_system',
    db.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), primary_key=True),
    db.Column('system_id', sa.Integer, sa.ForeignKey('systems.id'), primary_key=True)
)

game_publisher_association = db.Table('game_publisher',
    db.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), primary_key=True),
    db.Column('publisher_id', sa.Integer, sa.ForeignKey('publishers.id'), primary_key=True)
)