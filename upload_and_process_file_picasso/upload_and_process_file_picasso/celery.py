import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upload_and_process_file_picasso.settings')
app = Celery('upload_and_process_file_picasso')
# app.config_from_object('upload_and_process_file_picasso.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app = Celery('api')
# app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')