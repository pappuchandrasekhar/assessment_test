from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=255)
    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)
    choice_3 = models.CharField(max_length=255)
    choice_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

class Marks(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models. CASCADE)
    random_id = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models. CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)