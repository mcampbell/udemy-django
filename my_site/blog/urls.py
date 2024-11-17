"""
URLs for the Blog
/ => Welcome text, last 3 posts
/posts => List all posts
/posts/<slug> => Show a single post
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
