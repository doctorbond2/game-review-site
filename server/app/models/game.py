from app import db
import sqlalchemy as sa
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime

# class Game(db.Model):
#     __tablename__ = 'games'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120), unique=True, nullable=False)
#     release_year = db.Column(db.Integer, nullable=False)
#     publisher = db.Column(db.String(80), default='unknown')
#     studio = db.Column(db.String(80), default=publisher)
#     systems = db.Column(db.String(80), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Game(db.Model):
    __tablename__ = 'games'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    release_year: so.Mapped[int] = so.mapped_collection(sa.Integer)
    systems: so.Mapped['System'] = so.relationship(back_populates='games') # type: ignore
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())