from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.urls import reverse

month_names = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
challenges = dict(
    [(month, f"Your challenge for {month.title()}") for month in month_names]
)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "challenges/index.html", {"months": month_names})


# Create your views here.
def monthly_goal(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return render(
            request,
            "challenges/challenge.html",
            {
                "month": month,
                "challenge": challenges[month.lower()],
            },
        )
    except (KeyError, TemplateDoesNotExist):
        return HttpResponse("Invalid month.")


def monthly_goal_by_cardinal(request: HttpRequest, month: int) -> HttpResponse:
    # return monthly_goal(request, month_names[month - 1])

    month_name = month_names[month - 1]
    redirect_path = reverse("string-monthly-challenge", args=[month_name])
    return HttpResponseRedirect(redirect_path)
