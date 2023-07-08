from django.urls import path
from .views import *

urlpatterns = [
    path('', create_video, name='create_video')
]