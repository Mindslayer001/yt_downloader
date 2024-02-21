from django.urls import path
from .views import getVideoDescription, getDescription, downloadStream, home

urlpatterns = [
    path("", home, name='home'),
    path('video/', getDescription, name="video"),
    path('video/<str:url>', getVideoDescription, name="link-video"),
    path('download/<str:video_id>', downloadStream, name="download")
]