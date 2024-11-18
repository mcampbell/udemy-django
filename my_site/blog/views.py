from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse("List of posts")


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse(f"Post with slug: {slug}")
