from django.http import HttpResponse, HttpRequest

JAN_OUTPUT: str = "This works!"
FEB_OUTPUT: str = "Feb works!"

# Create your views here.
def january(request: HttpRequest) -> HttpResponse:
    return HttpResponse(JAN_OUTPUT)

def feb(request: HttpRequest) -> HttpResponse:
    return HttpResponse(FEB_OUTPUT)
