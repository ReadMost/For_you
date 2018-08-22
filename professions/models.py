from django.db import models

# Create your models here.

class Profession(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length = 100)
    profession = models.ForeignKey(Profession, on_delete = models.CASCADE)