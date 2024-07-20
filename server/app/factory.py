from app import db, app
from app.models import game, system, user, genre, publisher, review, association_tables
from app.models.game import Game
from app.models.system import System
from app.models.genre import Genre
from app.models.publisher import Publisher
from app.models.user import User
from app.models.publisher import Publisher

from sqlalchemy import select
def create_sample_data():
    print("Creating sample data")
    # Create sample data
    db.drop_all()
    db.create_all()
    
    # Create sample genres, systems, and publishers as dictionaries
    sample_genres = {
        'Action': Genre(name='Action'),
        'Adventure': Genre(name='Adventure'),
        'RPG': Genre(name='RPG'),
        'Simulation': Genre(name='Simulation'),
        'Strategy': Genre(name='Strategy'),
        'Sports': Genre(name='Sports'),
        'Puzzle': Genre(name='Puzzle'),
        'Platformer': Genre(name='Platformer'),
    }
    sample_publishers = {
        'Nintendo': Publisher(name='Nintendo', founded=1889),
        'Sony': Publisher(name='Sony', founded=1946),
        'Larian Studios': Publisher(name='Larian Studios', founded=1996),
    }
    nintendo = Publisher(name='Nintendo', founded=1889)
    sony = Publisher(name='Sony', founded=1946)
    playstation_5 = System( name='PlayStation 5', manufacturer=sony, release_year=2020)
    nes = System(id=1, name='NES', manufacturer=nintendo, release_year=1983)
    larian_studios = Publisher(id=2, name='Larian Studios', founded=1996)

    test_user = User(
        username='Uberlord_12', 
        email='uberlord123@hotmail.com')
    test_user_password = 'Password123!'
    test_user.set_password(test_user_password )

    sample_publishers['Nintendo'].systems = list([nes])
    sample_publishers['Sony'].systems = list([playstation_5])

    print(sample_publishers['Nintendo'].name)
    sample_games = {
        'Super Mario Bros.': Game(title='Super Mario Bros.', 
        release_year=1985, systems=[nes], 
        publisher=[sample_publishers['Nintendo']], 
        genre=[sample_genres['Action'],
               sample_genres['Platformer']]),

        'Baldur\'s Gate 3': Game(
        title='Baldur\'s Gate 3', 
        release_year=2020, 
        systems=[nes], 
        publisher=[sample_publishers['Larian Studios']], 
        genre=[sample_genres['RPG'],sample_genres['Strategy'], sample_genres['Adventure']],
        pc=True, 
        mac=True),

        'The Legend of Zelda':  Game(
        title='The Legend of Zelda', 
        release_year=1986, systems=[nes], 
        publisher=[sample_publishers['Nintendo']], 
        genre=[sample_genres['Action'], 
               sample_genres['Adventure']])
    }
    # super_mario_bros = Game(
    #     title='Super Mario Bros.', 
    #     release_year=1985, systems=[nes], 
    #     publisher=sample_publishers['Nintendo'], 
    #     genre=[sample_genres['Action'],]
    # )
    # baldurs_gate_3 = Game(
    #     title='Baldur\'s Gate 3', 
    #     release_year=2020, 
    #     systems=[nes], 
    #     publisher=sample_publishers['Larian Studios'], 
    #     genre=[sample_genres['RPG'],sample_genres['Strategy'], sample_genres['Adventure']],
    #     pc=True, 
    #     mac=True)

    # the_legend_of_zelda = Game(
    #     title='The Legend of Zelda', 
    #     release_year=1986, systems=[nes], 
    #     publisher=[nintendo], 
    #     genre=[sample_genres['Action'], 
    #            sample_genres['Adventure']
    # ])

    session = db.session()

   
    session.add_all(sample_genres.values())
    session.add_all(sample_publishers.values())
    session.add_all(sample_games.values())
    session.add(test_user)
    session.commit() 