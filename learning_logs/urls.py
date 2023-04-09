"""Определяет схемы URL для learning_logs"""
from django.urls import path, re_path
from .views import *

app_name = 'learning_logs'
urlpatterns = [
    path('', index, name='index'),
    path('topics/', topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    re_path('new_entry/(?P<topic_id>\d+)/', new_entry, name='new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/', edit_entry, name='edit_entry'),
]
