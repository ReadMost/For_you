from rest_framework import serializers
from . import models

class BulletSerializer( serializers.ModelSerializer ):
    class Meta:
        fields = (
            'id',
            'step',
            'description',
            'link_name',
            'link',
        )
        model = models.Bullet

class StepSerializer(serializers.ModelSerializer):
    bullet_set = BulletSerializer(many = True, read_only = True)
    class Meta:
        fields = (
            'id',
            'recommendation',
            'title',
            'bullet_set',
        )
        model = models.Step

class RecommendationSerializer(serializers.ModelSerializer):
    step_set = StepSerializer(many = True, read_only = True)
    class Meta:
        fields = (
            'id',
            'user',
            'profession',
            'title',
            'description',
            'created',
            'step_set',
        )
        model = models.Recommendation


