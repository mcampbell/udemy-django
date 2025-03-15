from django.views.generic import TemplateView, DetailView, ListView

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


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    # context_object_name = "post"
    # pk not required since we're using slug, and Django knows that and does it automatically.
