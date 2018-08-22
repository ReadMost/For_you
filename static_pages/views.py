from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'static_pages/index.html')


def notfound(request):
    return render(request, 'static_pages/notfound.html')