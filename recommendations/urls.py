from django.urls import path
from . import views

app_name = 'recommendations'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('index1/', views.index1, name = 'index1'),
    path('<int:recommendation_id>/', views.detail, name = 'detail'),
    path('add/', views.add, name = 'add'),
    path('<int:recommendation_id>/addstep', views.add_step, name = 'addstep'),
    path('like/<int:recommendation_id>/', views.like, name = 'like'),
    path('comment/', views.comment, name = 'comment'),
    path('saver/<int:recommendation_id>/', views.saver, name = 'saver'),
    path('<int:recommendation_id>/', views.detail, name = 'detail'),
]