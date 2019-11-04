from celery import Celery

app = Celery('tasks',broker='amqp://localhost:8000//')

@app.task
def reverse(string):
    return string