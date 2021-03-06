# -*- coding:utf-8 -*-
from rest_framework.pagination import PageNumberPagination


class MaterialPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100
