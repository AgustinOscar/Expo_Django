import datetime
from pyexpat import model
from time import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Pregunta')
    pub_date = models.DateTimeField(verbose_name='Fecha publicación', blank=True, null=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text