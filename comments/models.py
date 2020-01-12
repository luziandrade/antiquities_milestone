from django.db import models
from django.utils import timezone


class Question(models.Model):
    user = models.CharField(max_length=200)
    question = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __unicode__(self):
        return self.question
