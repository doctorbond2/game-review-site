from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
class Review(db.Model):
    __tablename__ = 'reviews'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    reviewer: so.Mapped['User'] = so.relationship( # type: ignore
        'User', back_populates='reviews')
    user_id: so.Mapped[int] = so.mapped_column(
        sa.Integer,sa.ForeignKey('users.id'), 
        index=True, nullable=False
    ) 
    game: so.Mapped['Game'] = so.relationship( # type: ignore
        'Game', back_populates='reviews' )
    game_id: so.Mapped[int] = so.mapped_column(
        sa.Integer, sa.ForeignKey('games.id'), 
        index=True, nullable=False)
    story_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    combat_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    voice_acting_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    open_world_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    weapons_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    level_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    combat_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    characters_score: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    final_score: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)

    __table_args__ = (
         sa.CheckConstraint( 
            'final_score >= 1 AND final_score <= 10',
            name='final_score_range_check'
        ),
    )