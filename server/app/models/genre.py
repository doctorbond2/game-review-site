from app import db
import sqlalchemy as sa
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_genre_association

class Genre(db.Model):
    __tablename__ = 'genres'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    games: so.Mapped['Game'] = so.relationship('Game', secondary=game_genre_association, back_populates='genres') # type: ignore
    def __repr__(self):
        return '<Genre {}>'.format(self.name)