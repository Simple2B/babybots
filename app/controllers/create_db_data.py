from app.models import User, Schedule


def create_db_data():
    User(username='admin', email='admin@gmail.com', password='admin').save()
    Schedule().save()
