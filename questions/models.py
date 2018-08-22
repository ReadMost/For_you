from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE),
    answer = models.CharField(max_length = 30)

    def __str__(self):
        return self.answer
class Question(models.Model):
    question_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_text
