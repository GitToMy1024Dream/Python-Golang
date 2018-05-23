from django.conf.urls.defaults import *
from django.views.generic import list_detail
from book.models import Publisher
from book.template_context import publisher_info_1, publisher_info_2, apress_books
from book.books_by_publisher import author_detail, books_by_publisher

urlpatterns = [
    (r'^publishers/$', list_detail.object_list, publisher_info_1),
    (r'books/$', list_detail.object_list, publisher_info_2),
    (r'apress_book/$', list_detail.object_list, apress_books),
    (r'^authors/(?P<author_id>\d+)/$', author_detail),
    (r'^books/(\w+)/$', books_by_publisher),
]
