from django.db import models
from django.utils import timezone


class Bid(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name
