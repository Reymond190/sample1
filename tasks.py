from celery import Celery

app = Celery('tasks',broker='amqp://user:**@rabbit1:5672//')

@app.task
def reverse(string):
    return string