from app import db
import sqlalchemy as sa
from sqlalchemy.schema import CheckConstraint
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_publisher_association, game_genre_association, game_system_association

class Game(db.Model):
    __tablename__ = 'games'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    release_year: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    publisher: so.WriteOnlyMapped['Publisher'] = so.relationship('Publisher', secondary='game_publisher', back_populates='games') # type: ignore
    genre: so.WriteOnlyMapped['Genre'] = so.relationship('Genre', secondary='game_genre', back_populates='games') # type: ignore    
    systems: so.WriteOnlyMapped['System'] = so.relationship('System', secondary='game_system', back_populates='games') # type: ignore
    pc: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    mac: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    image_url: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255), default='https://gamefaqs.gamespot.com/a/box/8/1/2/14812_front.jpg')
    __table_args__ = (
        CheckConstraint('release_year >= 1940 AND release_year <= 2024', name='release_year_check'),
        )