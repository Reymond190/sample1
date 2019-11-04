from celery import Celery

app = Celery('tasks',broker='amqp://rabbit1//')

@app.task
def reverse(string):
    return string[::-1]