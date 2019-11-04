from celery import Celery

app = Celery('tasks',broker='amqp://ec2-52-66-180-183.ap-south-1.compute.amazonaws.com//')

@app.task
def reverse(string):
    return string