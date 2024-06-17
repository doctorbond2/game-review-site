from app import db
import sqlalchemy as sa
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_genre_association

class Game(db.Model):
    __tablename__ = 'games'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    release_year: so.Mapped[int] = so.mapped_collection(sa.Integer)
    publisher: so.Mapped[str] = so.mapped_column(sa.String(80), default='unknown')
    genres: so.Mapped['Genre'] = so.relationship('Genre', secondary=game_genre_association, back_populates='games') # type: ignore    
    systems: so.Mapped['System'] = so.relationship('System', secondary='game_system', back_populates='games') # type: ignore
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())