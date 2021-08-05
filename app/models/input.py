from app import db
from app.models.utils import ModelMixin


class Input(db.Model, ModelMixin):
    __tablename__ = "inputs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Float, default=0.0)
    is_locked = db.Column(db.Boolean, default=False)
