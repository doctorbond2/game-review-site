from app import db, app
from app.models import game, system, user, genre, publisher, association_tables

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
    sample_systems = {
        'NES': system.System(name='NES'),
        'SNES': system.System(name='SNES'),
        'N64': system.System(name='N64'),
        'GameCube': system.System(name='GameCube'),
        'Wii': system.System(name='Wii'),
        'Wii U': system.System(name='Wii U'),
        'Switch': system.System(name='Switch'),
    }
    sample_publishers = {
        'Nintendo': publisher.Publisher(name='Nintendo', founded=1889),
        'Square Enix': publisher.Publisher(name='Square Enix', founded=1986),
        'Konami': publisher.Publisher(name='Konami', founded=1969),
        'Capcom': publisher.Publisher(name='Capcom', founded=1979),
        'Sega': publisher.Publisher(name='Sega', founded=1960),
        'Sony': publisher.Publisher(name='Sony', founded=1946),
        'Microsoft': publisher.Publisher(name='Microsoft', founded=1975),
    }

    # Create sample games using the dictionaries
    sample_games = [
    game.Game(title='Super Mario Bros.', 
              release_year=1985, 
              genre=[sample_genres['Adventure'], sample_genres['Action']],
              systems=[sample_systems['NES']],
              publisher=[sample_publishers['Nintendo']]),
    game.Game(title='The Legend of Zelda', 
              release_year=1986, 
              genre=[sample_genres['Adventure'], sample_genres['Action']],
              systems=[sample_systems['NES']],
              publisher=[sample_publishers['Nintendo']]),
    game.Game(title='Final Fantasy', 
              release_year=1987, 
              genre=[sample_genres['RPG'], sample_genres['Adventure']],
              systems=[sample_systems['NES']],
              publisher=[sample_publishers['Square Enix']]),
]

    # Add all sample data to the session and commit
    db.session.add_all(
        list(sample_genres.values()) 
        + list(sample_systems.values()) 
        + list(sample_publishers.values())
        + sample_games)
    db.session.commit()