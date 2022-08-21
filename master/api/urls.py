from django.urls import path,re_path

from .views import video_list_view

urlpatterns = [
    path('videos/', video_list_view),
    re_path('videos/(?P<query>.+)/$', video_list_view),
]