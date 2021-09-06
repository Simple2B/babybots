from app.models import User
from config import BaseConfig as conf


def register(username, email="username@test.com", password="password"):
    user = User(username=username, email=email, password=password)
    user.save()
    return user.id


def login(client, username=conf.ADMIN_USER_NAME, password=conf.ADMIN_USER_PASS):
    return client.post(
        "/login",
        data=dict(user_id=username, password=password, current_time=10),
        follow_redirects=True,
    )


def logout(client):
    return client.get("/logout", follow_redirects=True)
