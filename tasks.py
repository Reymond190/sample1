from celery import Celery

app = Celery('tasks',broker='amqp://locahost//')

@app.task
def reverse(string):
    return string