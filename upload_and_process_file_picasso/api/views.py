from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .models import File
from .serializers import FileSerializer


# class FileCreateList(generics.ListCreateAPIView):
#     """
#     POST - creates a File object
#     GET - returns list of all File objects
#     """
#     queryset = File.objects.all()
#     serializer_class = FileSerializer

class FileCreate(generics.CreateAPIView):
    """
    POST - creates a File object
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileList(generics.ListAPIView):
    """
    GET - returns list of all File objects
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer


# вьюсет базовый
# class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin):
#     """
#     POST - creates an object
#     GET - returns list of all objects
#     """
#     pass
