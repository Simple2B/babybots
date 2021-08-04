from datetime import datetime
from app.models import Schedule, Input
from app.logger import log


def set_running():
    """Set status run in data base"""
    schedule = Schedule.query.first()
    schedule.launch_status = True
    schedule.save()
    log(log.INFO, 'Status was set in data base')


def set_down():
    """Set status down in data base"""
    schedule = Schedule.query.first()
    schedule.launch_status = False
    schedule.save()
    log(log.INFO, 'Status was set in data base')


def main(func):
    """Main func for launch script"""
    schedule = Schedule.query.first()
    if schedule.launch_status:
        log(log.WARNING, 'Script is already running')
        return None
    db_launch_time = schedule.launch_time
    now = datetime.now().time()
    if db_launch_time.hour == now.hour and db_launch_time.minute == now.minute:
        log(log.INFO, 'Script starts')
        launch_script(func)
        log(log.INFO, 'Script stops')


def launch_script(func):
    """Launch the script"""
    inputs = Input.query.all()
    set_running()
    func(inputs)
    set_down()
    set_last_update()


def set_last_update():
    """Set last update in data base """
    schedule = Schedule.query.first()
    now = datetime.now().time()
    schedule.last_update = now
    schedule.save()
    log(log.INFO, 'Last update has been set in data base')


def get_last_update():
    """Get last update from data base"""
    schedule = Schedule.query.first()
    if not schedule.last_update:
        log(log.WARNING, 'No last update in data base')
        return 'Undefined'
    log(log.INFO, 'Get last update from data base')
    return schedule.last_update.strftime('%H:%M:%S')
