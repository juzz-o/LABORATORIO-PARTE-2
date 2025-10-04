from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    #image = models.ImageField(upload_to='movies/images/')
    image = models.ImageField(upload_to='movies/images', null=True, blank=True, default='default.jpg')
    url = models.URLField(blank=True)