# /api/urls.py
from booksapp.views import index, PostAPI
from django.urls import path

urlpatterns = [
    path("index/", index),
    path('posts/', PostAPI.as_view())
]