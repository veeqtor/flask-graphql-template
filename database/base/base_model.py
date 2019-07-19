"""Base class model"""

# system imports
from datetime import datetime

# local imports
from database import db
from database.base.model_operations import ModelOperation


class BaseModel(db.Model, ModelOperation):
    """
    base model
    """

    __abstract__ = True

    id = db.Column(db.String(36), unique=True, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    deleted = db.Column(db.Boolean, default=False)
