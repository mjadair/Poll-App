from django.db import models

# Create your models here.


#The first positional argument of each of the fields can be changed to a human readable format.
#This is the case with Question in the Choice model. 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
