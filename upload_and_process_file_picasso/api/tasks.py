from celery import shared_task

from upload_and_process_file_picasso.celery import app
from .models import File


@shared_task
def change_processed(file_obj_id):
    """
    Changes field 'processed' to True in
    newly created File objects.
    Expected to be called by FileCreate in views.
    """
    try:
        processed_file = File.objects.get(pk=file_obj_id)
        processed_file.processed = True
        processed_file.save()
    except DoesNotExist:
        pass