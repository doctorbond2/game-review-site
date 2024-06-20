from app import db
import sqlalchemy as sa
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    founded: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    systems: so.WriteOnlyMapped['System'] = so.relationship('System', back_populates='manufacturer') # type: ignore
    games: so.WriteOnlyMapped['Game'] = so.relationship('Game', secondary='game_publisher', back_populates='publisher') # type: ignore
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    def __repr__(self):
        return '<Publisher {}>'.format(self.name)