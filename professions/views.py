from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'professions/index.html')
def all(request):
    users = User.objects.all()
    return render(request, 'professions/all.html',{'users': users})

