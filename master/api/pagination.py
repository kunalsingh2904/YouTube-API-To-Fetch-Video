from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'p_size'
    max_page_size = 1000