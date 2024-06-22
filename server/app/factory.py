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
    nintendo = publisher.Publisher(id=1 , name='Nintendo', founded=1889)
    nes = system.System(id=1, name='NES', manufacturer=nintendo, release_year=1983)
    nintendo.systems = list([nes])

    super_mario_bros = game.Game(
        title='Super Mario Bros.', release_year=1985, systems=[nes], publisher=[nintendo]
    )
    session = db.session()
    session.add(nintendo)
    session.add_all(sample_genres.values())
    session.commit() 