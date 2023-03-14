from django.db import models
from quizzes.models import Quiz
import random

# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.DO_NOTHING, related_name="quizses")
    score = models.IntegerField()