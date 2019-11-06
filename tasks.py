from celery import Celery

app = Celery('tasks',broker='amqp://0.0.0.0:5672//')

@app.task
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str