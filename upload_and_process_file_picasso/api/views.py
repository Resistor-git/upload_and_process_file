from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .models import File
from .serializers import FileSerializer
from .tasks import change_processed


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

    def form_valid(self, form):
        print('!!!!!!!!!!!!', flush=True)
        return super().form_valid(form)


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
