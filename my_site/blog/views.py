from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/all-posts.html")


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    return render(request, "blog/post-detail.html")
