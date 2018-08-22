from django.urls import path
from . import views

app_name = 'static_pages'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('notfound/', views.notfound, name = 'notfound')
]