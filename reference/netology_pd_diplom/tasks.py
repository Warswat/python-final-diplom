import time
from celery import Celery

app = Celery(broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/1',
             broker_connection_retry_on_startup=True)



@app.task()
def add(x, y):


    return x + y

