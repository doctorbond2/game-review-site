from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,nullable=False)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))
    reviews: so.WriteOnlyMapped['Review'] = so.relationship( # type: ignore
        'Review', back_populates='reviewer')
    

    _table_args__ = (
        sa.CheckConstraint( 
            "password ~ '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$'",
            name='password_complexity_check'
        ),
        sa.CheckConstraint(
            'char_length(username) >= 5 AND char_length(username) <= 64'
        ),
        sa.CheckConstraint(
            'char_length(password) >= 8 AND char_length(password) <= 256'
        )
    )

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
            
        }
    def to_dict_with_reviews(self,session):
        from .review import Review
        reviews = session.query(Review).filter(Review.user_id == self.id).all()
        return {
            "username": self.username,
            "email": self.email,
            "reviews": [review.to_dict() for review in reviews]
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)
