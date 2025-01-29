from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review


class ReviewView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        # create a new empty form to show in the case of a GET. We need to use the same variable name as the POST
        # request so that can just render WHATEVER form happens to get picked based on HTTP method.
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ReviewForm(request.POST)
        if form.is_valid():
            # This is a ModelForm so can save directly.
            form.save()

            # everything's cool, move ahead.
            return HttpResponseRedirect("/thank-you")

        else:
            return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_context"] = "Thanks so much for your review!"
        return context

class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context

class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(pk=kwargs["pk"])
        context["review"] = review
        return context
