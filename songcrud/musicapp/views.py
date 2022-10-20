from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello there, I made my first django app - musicapp")