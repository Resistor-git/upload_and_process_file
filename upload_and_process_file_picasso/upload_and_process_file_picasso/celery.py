import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upload_and_process_file_picasso.settings')
app = Celery('upload_and_process_file_picasso')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
