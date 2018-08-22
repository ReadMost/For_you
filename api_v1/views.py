from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from recommendations import models
from recommendations import serializers
from django.contrib.auth.models import User


# RECOMMENDATIONS
class ListCreateRecommendation(generics.ListCreateAPIView):
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class RetriveUpdateDestroyRecommendation(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Recommendation.objects.all()
    serializer_class = serializers.RecommendationSerializer

#STEPS
class ListCreateStep(generics.ListCreateAPIView):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer

    def get_queryset(self):
        return self.queryset.filter(recommendation_id = self.kwargs.get('recommendation_pk'))

    def perform_create(self, serializer):
        recommendation = get_object_or_404(
            models.Recommendation, pk = self.kwargs.get('recommendation_pk'))
        if(recommendation.user != self.request.user):
            raise ValidationError('This is recommendation belong to other person')
        serializer.save(recommendation = recommendation)

#BULLET
class ListCreateBullet(generics.ListCreateAPIView):
    queryset = models.Bullet.objects.all()
    serializer_class = serializers.BulletSerializer

    def get_queryset(self):
        step = get_object_or_404(models.Step,
                    recommendation_id = self.kwargs.get('recommendation_pk'),
                    pk = self.kwargs.get('step_pk'))
        return self.queryset.filter(step_id = self.kwargs.get('step_pk'))
    
    def perform_create(self, serializer):
        recommendation = get_object_or_404(
            models.Recommendation, pk = self.kwargs.get('recommendation_pk'))
        if(recommendation.user != self.request.user):
            raise ValidationError('This is recommendation belong to other person')
        step = get_object_or_404(
            models.Step, pk = self.kwargs.get('step_pk'))
        if(step.recommendation != recommendation):
            raise ValidationError('This Step belong to other recommendation')
        serializer.save(step = step)