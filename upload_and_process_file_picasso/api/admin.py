from django.contrib import admin

from .models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'file', 'uploaded_at', 'processed']
    list_editable = ['processed']
    list_filter = ['processed']