from upload_and_process_file_picasso.celery import app

from .models import File


@app.task
def change_processed(file_obj):
    processed_file = File.objects.get(pk=file_obj.pk)
    processed_file.processed = True





# from celery import shared_task
#
# @shared_task
# def shared_task():
#     return