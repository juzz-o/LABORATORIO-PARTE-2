from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    release_date = models.ImageField()
    url = models.URLField(blank=True)