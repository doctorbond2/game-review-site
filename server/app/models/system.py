from app import db
import sqlalchemy as sa
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime, timezone

class System(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    manufacturer: so.Mapped[str] = so.mapped_column(sa.String(80), nullable=False)
    release_year: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    games: so.WriteOnlyMapped['Game'] = so.relationship(back_populates='games') # type: ignore
    def __repr__(self):
        return '<System {}>'.format(self.name)
