from rest_framework.pagination import PageNumberPagination

class NewPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'page'
    page_size_query_param = 'per_page'