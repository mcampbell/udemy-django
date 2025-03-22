from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView

from .forms import CommentForm
from .models import Post


# This could also be a ListView since we're getting an abbreviated list of Posts.  We'd still have to override
# get_queryset, to do the limiting.
class WelcomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.order_by("-date")[:3]
        context["posts"] = latest_posts
        return context


class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "post_list"
    ordering = ["-date"]


class PostDetailView(View):
    def get(self, request, slug=None):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug=None):
        # We get the slug because it's already part of the URL that got us here
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            transient = comment_form.save(commit=False)
            transient.post = post
            transient.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        else:
            context = {
                "post": post,
                "comment_form": CommentForm(),
            }
            return render(request, "blog/post-detail.html", context)
