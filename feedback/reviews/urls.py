from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view(), name="review-list"),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
]
