from django.db import models

# Create your models here.
class VideoDetail(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    published_datetime = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=1000)
    video_id = models.CharField(max_length=100, unique=True)
    channel_name = models.CharField(max_length=150)
    channel_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title