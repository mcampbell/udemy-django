from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm

# Create your views here.


def store_file(file):
    with open("/tmp/" + file.name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        print(request.FILES["user_image"])
        store_file(request.FILES["user_image"])
        return HttpResponseRedirect("/profiles")
