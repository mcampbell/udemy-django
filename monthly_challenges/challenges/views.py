from configparser import Error

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

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
challenges = dict([(month, f"Your challenge for {month.title()}") for month in month_names])



# Create your views here.
def monthly_goal(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return HttpResponse(challenges[month])
    except Error:
        return HttpResponse("Invalid month.")

def monthly_goal_by_cardinal(request: HttpRequest, month: int) -> HttpResponse:
    # return monthly_goal(request, month_names[month - 1])
    return HttpResponseRedirect(f"/challenges/{month_names[month - 1]}")
