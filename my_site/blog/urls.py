"""
URLs for the Blog
/ => Welcome text, last 3 posts
/posts => List all posts
/posts/<slug> => Show a single post
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.WelcomeView.as_view(), name="welcome"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
