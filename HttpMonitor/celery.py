import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HttpMonitor.settings')

app = Celery('HttpMonitor')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a CELERY_ prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'my_task': {
        'task': 'core.tasks.my_task',
        # every 30 seconds
        'schedule': crontab(minute='*/30'),
    },
}
