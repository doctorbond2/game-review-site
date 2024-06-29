from app import db
import sqlalchemy as sa
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_publisher_association as gpa

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    founded: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    systems: so.WriteOnlyMapped['System'] = so.relationship('System', back_populates='manufacturer') # type: ignore
    games: so.WriteOnlyMapped['Game'] = so.relationship('Game', secondary='game_publisher', primaryjoin=(gpa.c.publisher_id == id), secondaryjoin=(gpa.c.game_id == id)) # type: ignore
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'founded': self.founded,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    def __repr__(self):
        return '<Publisher {}>'.format(self.name)