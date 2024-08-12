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

    def to_dict(self):
        data = {
            'id': self.id,
            'reviewer_id': self.user_id,
            'game_id': self.game_id,
            'final_score': self.final_score,
        }
        if self.story_score is not None:
            data['story_score'] = self.story_score
        if self.combat_score is not None:
            data['combat_score'] = self.combat_score
        if self.voice_acting_score is not None:
            data['voice_acting_score'] = self.voice_acting_score
        if self.open_world_score is not None:
            data['open_world_score'] = self.open_world_score
        if self.weapons_score is not None:
            data['weapons_score'] = self.weapons_score
        if self.level_score is not None:
            data['level_score'] = self.level_score
        if self.combat_score is not None:
            data['combat_score'] = self.combat_score
        if self.characters_score is not None:
            data['characters_score'] = self.characters_score

        return data
    
    __table_args__ = (
         sa.CheckConstraint( 
            'final_score >= 1 AND final_score <= 10',
            name='final_score_range_check'
        ),
        
    )