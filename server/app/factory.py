from app import db, app
from app.models import game, system, user, genre, publisher, association_tables
from sqlalchemy import select
def create_sample_data():
    print("Creating sample data")
    # Create sample data
    db.drop_all()
    db.create_all()
    
    # Create sample genres, systems, and publishers as dictionaries
    sample_genres = {
        'Action': genre.Genre(name='Action'),
        'Adventure': genre.Genre(name='Adventure'),
        'RPG': genre.Genre(name='RPG'),
        'Simulation': genre.Genre(name='Simulation'),
        'Strategy': genre.Genre(name='Strategy'),
        'Sports': genre.Genre(name='Sports'),
        'Puzzle': genre.Genre(name='Puzzle'),
    }
    nintento_systems = {
        'NES': system.System(name='NES',),
    }
    sony_systems = {
        'PlayStation': system.System(name='PlayStation'),
        'PlayStation 2': system.System(name='PlayStation 2'),
        'PlayStation 3': system.System(name='PlayStation 3'),
        'PlayStation 4': system.System(name='PlayStation 4'),
    }
    sample_systems = {
        'NES': system.System(name='NES', release_year=1983),
    }
    sample_publishers = {
        'Nintendo': publisher.Publisher(
            name='Nintendo', 
            founded=1889,
            systems=list(nintento_systems.values())),
    }
    sample_systems_with_publisher = {
    'NES': system.System(name='NES', release_year=1983, manufacturer=sample_publishers['Nintendo']),
}
    sample_games = [
        game.Game(title='Super Mario Bros.', 
                  release_year=1985, 
                  genre=[sample_genres['Adventure'], sample_genres['Action']],
                  systems=[sample_systems_with_publisher['NES']],
                  publisher=[sample_publishers['Nintendo']]),
        game.Game(title='The Legend of Zelda', 
                  release_year=1986, 
                  genre=[sample_genres['Adventure'], sample_genres['Action']],
                  systems=[sample_systems_with_publisher['NES']],
                  publisher=[sample_publishers['Nintendo']]),
        game.Game(title='Final Fantasy', 
                  release_year=1987, 
                  genre=[sample_genres['RPG'], sample_genres['Adventure']],
                  systems=[sample_systems_with_publisher['NES']],
                  publisher=[sample_publishers['Square Enix']]),
    ]
    session = db.session()
    # Add all sample data to the session and commit
    session.add_all(
        list(sample_genres.values()) 
        + list(sample_systems_with_publisher.values()) 
        + list(sample_publishers.values())
        + sample_games)
    session.commit()