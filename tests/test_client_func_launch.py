from datetime import datetime
import pytest
import time

from app import db, create_app
from app.controllers.create_db_data import create_db_data
from .utils import login
from app.models import Schedule


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


def call_client_func():
    time.sleep(10)


def test_launch_post(client):
    login(client)
    DELTA_HOURS = 5
    now = datetime.now()
    frontend_date = datetime(now.year, now.month, now.day, now.hour, now.minute)
    data = dict(
        launch_time=now.strftime("%H:%M"),
        value1=56,
        value2=56,
        value3=56,
        value4=56,
        value5=56,
        value6=56,
        value7=56,
        value8=56,
        value9=56,
        value10=56,
        checkbox1=False,
        checkbox2=False,
        checkbox3=False,
        checkbox4=False,
        checkbox5=False,
        checkbox6=False,
        checkbox7=False,
        checkbox8=False,
        checkbox9=False,
        checkbox10=False,
        submit_manual=True,
    )
    response = client.post(
        "/",
        data=data,
    )
    assert response.status_code == 200
    s: Schedule = Schedule.query.first()
    assert s
    assert s.is_run_now
    del data["submit_manual"]
    data["submit"] = True
    response = client.post(
        "/",
        data=data,
    )
    s: Schedule = Schedule.query.first()
    assert s
