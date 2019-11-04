from celery import Celery

app = Celery('tasks',broker='amqp://localhost:5672//')

@app.task
def reverse(string):
    return string