from statistics import mode
from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.headline
    