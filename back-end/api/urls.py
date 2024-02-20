from django.urls import path
from .views import getVideoDescription, getDescription, downloadStream

urlpatterns = [
    path('video/', getDescription, name="video"),
    path('video/<str:url>', getVideoDescription, name="link-video"),
    path('download/<int:itag>/<str:videoId>/', downloadStream, name="download")
]