from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()  # for rendering
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()

        return HttpResponseRedirect("/profiles")
