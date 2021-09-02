from datetime import datetime
from app.models import Schedule, Input
from app.logger import log
from flask.login import current_user


def set_running():
    """Set status run in data base"""
    schedule = Schedule.query.first()
    schedule.is_run = True
    schedule.save()
    log(log.INFO, "Status was set in data base")


def set_down():
    """Set status down in data base"""
    schedule = Schedule.query.first()
    schedule.is_run = False
    schedule.is_run_now = False
    schedule.save()
    log(log.INFO, "Status was set in data base")


def main(func):
    """Main func for launch script"""
    schedule = Schedule.query.first()
    if schedule.is_run:
        log(log.WARNING, "Script is already running")
        return None
    db_launch_time = schedule.launch_time
    now = datetime.now().time()
    if schedule.is_run_now or (
        db_launch_time
        and (db_launch_time // 60) == now.hour
        and (db_launch_time % 60) == now.minute
    ):
        log(log.INFO, "Script starts")
        launch_script(func)
        log(log.INFO, "Script stops")
    else:
        log(log.WARNING, "NOT RUN")


def launch_script(func):
    """Launch the script"""
    inputs = Input.query.all()
    set_running()
    vals = [input.value for input in inputs]
    try:
        func(*vals)
    finally:
        set_down()
        set_last_update()


def set_last_update():
    """Set last update in data base"""
    schedule = Schedule.query.first()
    now = datetime.now()
    schedule.last_update = now.minute + (now.hour + current_user.delta_time_hours) * 60
    schedule.save()
    log(log.INFO, "Last update has been set in data base [%s]", now)


def get_last_update() -> str:
    """Get last update from data base"""
    schedule = Schedule.query.first()
    if not schedule.last_update:
        log(log.WARNING, "No last update in data base")
        return "Undefined"
    log(log.INFO, "Get last update from data base")
    last_update_hours = schedule.last_update // 60
    last_update_minutes = schedule.last_update % 60
    if len(str(last_update_minutes)) == 1:
        last_update_minutes = '0' + str(last_update_minutes)
    else:
        last_update_minutes = str(last_update_minutes)
    return str(last_update_hours) + ':' + last_update_minutes
