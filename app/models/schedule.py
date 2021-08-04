from sqlalchemy.dialects.mysql import TIME
from app import db
from app.models.utils import ModelMixin


class Schedule(db.Model, ModelMixin):
    __tablename__ = "schedule"

    id = db.Column(db.Integer, primary_key=True)
    launch_time = db.Column(TIME, nullable=True)
    launch_status = db.Column(db.Boolean, default=False)
    last_update = db.Column(TIME, nullable=True)
    manual_start = db.Column(db.Boolean, default=False)
