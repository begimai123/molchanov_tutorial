
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1> HEllo petal in the dawn </h1>')
