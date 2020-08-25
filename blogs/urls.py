"""Defines URL patterns for blogs."""

from django.urls import path, re_path
from . import views

urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    #Shows all the blogs titles written by a user
    re_path(r'^posts/$', views.posts, name='posts'),
    re_path(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),
    re_path(r'^add_post/$', views.add_post, name='add_post'),
    re_path(r'^entry_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]
