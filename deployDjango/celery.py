# project/celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deployDjango.settings')

app = Celery('deployDjango')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
