from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileCreate, FileList

app_name = 'api'

urlpatterns = [
    path('upload/', FileCreate.as_view()),
    path('files/', FileList.as_view()),
]
