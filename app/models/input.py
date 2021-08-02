from app import db
from app.models.utils import ModelMixin


class Input(db.Model, ModelMixin):
    __tablename__ = "inputs"

    id = db.Column(db.Integer, primary_key=True)
    input_name = db.Column(db.String(60), nullable=True)
    input_value = db.Column(db.Float, nullable=True, default=0)
    is_locked = db.Column(db.Boolean, nullable=False, default=False)
