import pytest
from datetime import datetime

from app import db, create_app
from app.controllers.create_db_data import create_db_data


@pytest.fixture
def client():
    app = create_app(environment="testing")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        db.drop_all()
        db.create_all()
        create_db_data()
        yield client
        db.session.remove()
        db.drop_all()
        app_ctx.pop()


def test_delta_count():
    now = datetime.now().hour
    for i in range(0, 23):
        delta = (now - i + 24) % 24
        assert delta >= 0 and delta <= 23
