from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm


def review(request):
    # We have both a post (submits a review) and a get (displays the review form) request.
    if request.method == "POST":
        posted_form = ReviewForm(request.POST)
        if posted_form.is_valid():
            print(posted_form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    # We purposely don't do an else here, which gives us the ability to re-display the form if the request was a POST,
    # but it fails validation and falls through to here, *OR* if it's a GET, which is the more common case.
    review_form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": review_form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
