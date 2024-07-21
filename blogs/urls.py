from django.urls import re_path
from .views import post_list, post_detail


urlpatterns = [
    re_path(r'^$', post_list, name='blog_post_list'),
    re_path(
        r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>\[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
]
