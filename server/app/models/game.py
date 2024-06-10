from app.db import db
from datetime import datetime    

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(80), default='unknown')
    studio = db.Column(db.String(80), default=publisher)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    

    