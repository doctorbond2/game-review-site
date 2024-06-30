from app import db
import sqlalchemy as sa
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_genre_association as gga
class Genre(db.Model):
    __tablename__ = 'genres'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    games: so.WriteOnlyMapped['Game'] = so.relationship('Game', # type: ignore
        secondary=gga, back_populates='genre')
    
    def to_dict(self):
        return {
            'name': self.name,
        }
    def to_dict_with_details(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    def to_dict_with_games(self, session):
        from .game import Game
        games = session.scalars(sa.select(Game).join(gga).filter(gga.c.genre_id == self.id)).all()
        return {
            'name': self.name,
            'games': [{'title': game.title, 'release_year': game.release_year} for game in games]
        }

    def __repr__(self):
        return '<Genre {}>'.format(self.name)