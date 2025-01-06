from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    # We have both a post (submits a review) and a get (displays the review form) request.
    if request.method == "POST":
        # We will need to process the form data.
        username = request.POST["username"]
        return HttpResponseRedirect("/thank-you")

    else:
        return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")
