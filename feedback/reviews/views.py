from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


def review(request):
    # We have both a post (submits a review) and a get (displays the review form) request.
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # save the review to the database
            # create the Model from the form data
            clean = form.cleaned_data
            review_model = Review(
                username=clean["username"],
                review=clean["review"],
                rating=clean["rating"],
            )
            # then save to the db
            review_model.save()

            # everything's cool, move ahead.
            return HttpResponseRedirect("/thank-you")

    else:
        # create a new empty form to show in the case of a GET. We need to use the same variable name as the POST
        # request so that can just render WHATEVER form happens to get picked based on HTTP method.
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
