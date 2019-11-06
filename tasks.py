from celery import Celery

app = Celery('tasks',broker='amqp://reymond:reymond201@localhost/ray_vhost')

@app.task
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str