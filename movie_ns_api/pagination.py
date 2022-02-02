from rest_framework.pagination import PageNumberPagination

class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 10    
    max_page_size = 100
    page_size_query_param = 'limit'
    page_query_param = 'page'