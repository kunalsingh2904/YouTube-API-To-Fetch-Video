from rest_framework import serializers

from .models import VideoDetails

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetails
        fields = '__all__'