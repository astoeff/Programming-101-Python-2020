import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    price = models.IntegerField(default=100, unique=True)

    def __str__(self):
        return str(self.price)


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @property
    def votes(self):
        votes = 0
        for choice in self.choice_set.all():
            votes += choice.votes
        return votes

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
