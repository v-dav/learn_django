from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.TextField()
