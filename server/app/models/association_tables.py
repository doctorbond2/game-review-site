from app import db
import sqlalchemy as sa

# Association table for the many-to-many relationship between Game and Genre
game_genre_association = sa.Table(
    'game_genre', 
    db.metadata, 
    sa.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), 
                           primary_key=True),
    sa.Column('genre_id', sa.Integer, sa.ForeignKey('genres.id'),
                           primary_key=True)    
    )

game_system_association = sa.Table(
    'game_system', 
    db.metadata, 
    sa.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), 
                           primary_key=True),
    sa.Column('system_id', sa.Integer, sa.ForeignKey('systems.id'),
                            primary_key=True),)

game_publisher_association = sa.Table(
    'game_publisher', 
    db.metadata, 
    sa.Column('game_id', sa.Integer, sa.ForeignKey('games.id'), 
                           primary_key=True ),
    sa.Column('publisher_id', sa.Integer, sa.ForeignKey('publishers.id'),
                            primary_key=True))
