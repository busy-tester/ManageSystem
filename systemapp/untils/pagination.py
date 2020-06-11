from rest_framework import pagination


class MyPaginator(pagination.PageNumberPagination):
    page_size = 10  # 每页显示两条
    page_query_param = 'page'  # 页数的参数名为page
    page_size_query_param = 'size'  # 条数的参数为size
    max_page_size = 10  # 每页的条数最大不超过3条


class LimitOffsetPaginator(pagination.LimitOffsetPagination):
    default_limit = 1  # 默认显示的条数
    limit_query_param = 'limit'  # url里显示条数的参数名
    offset_query_param = 'offset'  # url里显示偏移位置的参数名


class CursorPaginatior(pagination.CursorPagination):
    cursor_query_param = 'cursor'
    ordering = '-id'  # 按id降序排
    page_size = 2  # 每页显示两条
