from django.db import models

# Create your models here.
class VideoDetails(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    published_datetime = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=1000)
    video_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title