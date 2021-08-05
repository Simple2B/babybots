from app.models import User, Schedule, Input
from config import BaseConfig as conf


def create_db_data():
    """Fill default data in data base"""
    User(
        username=conf.ADMIN_USER_NAME,
        email=conf.ADMIN_USER_EMAIL,
        password=conf.ADMIN_USER_PASS,
    ).save()
    Schedule().save()
    for i in range(1, 9):
        Input(name=f"value{i}").save()
