from datetime import datetime
from app.models import Schedule


def set_running():
    schedule = Schedule.query.all()[0]
    schedule.launch_status = True
    schedule.save()


def set_down():
    schedule = Schedule.query.all()[0]
    schedule.launch_status = False
    schedule.save()


def launch_script(func):
    schedule = Schedule.query.all()[0]
    db_launch_time = schedule.launch_time
    now = datetime.now().time()
    if db_launch_time.hour == now.hour and db_launch_time.minute == now.minute:
        func()
