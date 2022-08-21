from django.contrib import admin

# Register your models here.
from .models import VideoDetail

admin.site.site_header = "YouTube Video DashBoard"

class VideoDetailManager(admin.ModelAdmin):
    list_display = (
        'video_id',
        'title',
        'channel_name',
        'published_datetime',
        'thumbnail_url'
    )
    search_fields = ['title', 'channel_name']
    list_filter = ['channel_name']


admin.site.register(VideoDetail, VideoDetailManager)