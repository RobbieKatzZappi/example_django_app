
from django.http import HttpResponse

def index(request):
    return HttpResponse("client management index")
