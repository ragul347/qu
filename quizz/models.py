from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Quizques(models.Model):
    subject_name=models.CharField(max_length=10)
    question_no=models.CharField(max_length=3)
    questions=models.CharField(max_length=500)
    a=models.CharField(max_length=50)
    b=models.CharField(max_length=50)
    c=models.CharField(max_length=50)
    d=models.CharField(max_length=50)
    ans=models.CharField(max_length=50)
    des=models.CharField(max_length=100)
