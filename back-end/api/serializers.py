from rest_framework.serializers import ModelSerializer
from .models import Yt_Video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Yt_Video
        fields = "__all__"