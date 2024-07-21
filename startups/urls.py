from django.urls import re_path

from .views import startup_detail, tag_list, tag_detail, startups_list

urlpatterns = [
    re_path(r'^tag/$', tag_list),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail),
    re_path(r'^startup/$', startups_list),
    re_path(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail),
]
