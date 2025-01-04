from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

posts = Post.objects.all()


def get_date(post):
    return post.date

def get_posts_from_db():
    pass

# Create your views here.
def welcome(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def post_list(request: HttpRequest) -> HttpResponse:
    sorted_posts = Post.objects.order_by("-date")
    return render(request, "blog/all-posts.html", {"post_list": sorted_posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = get_object_or_404(Post, Q(slug=slug))
    return render(request, "blog/post-detail.html", {"post": post})
