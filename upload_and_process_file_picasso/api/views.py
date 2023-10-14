from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .models import File
from .serializers import FileSerializer
from .tasks import process


class FileCreate(generics.CreateAPIView):
    """
    POST - creates a File object.
    After object is created, it is processed by celerity task.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        file_obj = serializer.save()
        process.delay(file_obj.id)


class FileList(generics.ListAPIView):
    """
    GET - returns list of all File objects
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
