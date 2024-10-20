import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # object name = field name. column name
    question_text = models.CharField(max_length=200)
    
    # if supplied, first unnamed argument is human friendly name
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    # can also define relationships
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text