from django.http import HttpResponse, HttpRequest


# Create your views here.
def monthly_goal(request: HttpRequest, month: str) -> HttpResponse:
    return HttpResponse(f"My goal for {month}.")


def monthly_goal_by_cardinal(request: HttpRequest, month: int) -> HttpResponse:
    return HttpResponse(f"My goal for the month number {month}.")
