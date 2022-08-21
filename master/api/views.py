from django.shortcuts import render

from rest_framework.generics import ListAPIView
from django.db.models import Q

from .pagination import CustomPagination
from .models import VideoDetail
from .serializers import VideoDetailSerializer
# Create your views here.

class VideoDetailListAPIView(ListAPIView):
    serializer_class = VideoDetailSerializer
    model = VideoDetail
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            # Add other serach field if required
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset.order_by('-published_datetime')


video_list_view = VideoDetailListAPIView.as_view()