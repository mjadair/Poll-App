from django.db import models

# Create your models here.


class Question(models.model):
    question_text = models.charField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.charField(max_length=200)
    votes = models.IntegerField(default=0)
