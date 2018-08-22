from django.urls import path
from . import views

app_name = 'api_v1'
urlpatterns = [
    path('recommendations/', views.ListCreateRecommendation.as_view(), name = 'recommendations'),
    path('recommendations/<int:pk>/', views.RetriveUpdateDestroyRecommendation.as_view(), name = 'recommendation'),
    path('recommendations/<int:recommendation_pk>/steps/', views.ListCreateStep.as_view()),
    path('recommendations/<int:recommendation_pk>/steps/<int:step_pk>/bullets/',views.ListCreateBullet.as_view())
]