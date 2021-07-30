from app.models import User, Schedule, Input


def create_db_data():
    User(username='admin', email='admin@gmail.com', password='admin').save()
    Schedule().save()
    for i in range(1, 9):
        Input(input_name=f"value{i}").save()
