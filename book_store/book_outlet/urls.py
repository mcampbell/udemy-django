from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:id>", views.book_detail, name="book_detail"),
    path("book/<slug:slug>", views.book_detail_by_slug, name="book_detail_by_slug"),
]
