from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
import time

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_context"] = "Thanks so much for your review!"
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = str(time.asctime(time.localtime()))
        context["now"] = now
        return context


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
