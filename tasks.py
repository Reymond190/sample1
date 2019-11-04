from celery import Celery

app = Celery('tasks',broker='amqp://guest@rabbitmq1:5672//')

@app.task
def reverse(string):
    return string