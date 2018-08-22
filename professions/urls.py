from django.urls import path
from . import views

app_name = 'professions'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('all/', views.all, name = 'all')
]