from django.views.generic.edit import CreateView

from .models import UserProfile


# Create your views here.


class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
