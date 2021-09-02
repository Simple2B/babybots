from app import db
from app.models.utils import ModelMixin

TIME = db.Integer  # value: hours * 60 + minutes


class Schedule(db.Model, ModelMixin):
    __tablename__ = "schedule"

    id = db.Column(db.Integer, primary_key=True)
    launch_time = db.Column(TIME, default=0)
    is_run = db.Column(db.Boolean, default=False)
    last_update = db.Column(TIME, nullable=True)
    is_run_now = db.Column(db.Boolean, default=False)
