from django.db import models

# Create your models here.
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

from django.db import models
from django.utils import timezone
import datetime

#class Question(models.Model):
#    # ...
#    def __str__(self):
#        return self.question_text

class Question(models.Model):
    question_text, pub_date = models.CharField(max_length=200), models.DateTimeField('date published')
    
    # ToString Method
    def __str__(self):
        return self.question_text

    # Recently Published Check
    def was_published_recently(self): # from django tutorial
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Required fields: question, choice_text, votes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # ToString Method
    def __str__(self):
        return self.choice_text
