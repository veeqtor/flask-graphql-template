"""User model"""

# local import
from database import db
from database.base.base_model import BaseModel


class User(BaseModel):
    """
    User model
    """

    # table name
    __tablename__ = 'users'

    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.email)
