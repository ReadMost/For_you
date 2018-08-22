from django.db import models
from django.contrib.auth.models import User
from professions.models import Profession
# Create your models here.

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Step(models.Model):
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Bullet(models.Model):
    step = models.ForeignKey(Step, on_delete = models.CASCADE)
    description = models.TextField()
    link_name = models.CharField(max_length = 200)
    link = models.CharField(max_length = 350) 
    def __str__(self):
        return self.description

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return self.text
    

class Saver(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)
