import time
from app.logger import log


def client_func(*args):
    log(log.INFO, "Client func start")
    log(log.INFO, "Args: [%s]", args)
    time.sleep(60)
