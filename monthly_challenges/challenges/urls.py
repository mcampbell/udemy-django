from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.monthly_goal_by_cardinal),
    path("<str:month>", views.monthly_goal),
]
