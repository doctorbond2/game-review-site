from app import db
import sqlalchemy as sa
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_genre_association

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    systems: so.WriteOnlyMapped['System'] = so.relationship('System', back_populates='manufacturer') # type: ignore