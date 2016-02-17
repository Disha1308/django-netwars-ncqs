from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 200)
    choice_correct = models.CharField(max_length = 100)
    choice1 = models.CharField(max_length = 100)
    choice2 = models.CharField(max_length = 100)
    choice3 = models.CharField(max_length = 100)
    QUESTION_TYPE = (
            ("EASY", "easy type"),
            ("HARD", "hard type"),
        )
    question_type = models.CharField(max_length = 4, choices = QUESTION_TYPE, default="EASY")
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.question + "--->"+self.choice_correct   

class QuestionPaper(models.Model):
    user = models.ForeignKey(User);
    question = models.ForeignKey(Question);
    user_answer = models.CharField(max_length = 100, default='');
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return str(self.user)+" gave answer "+self.user_answer;

