from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True, max_length=3000)
    image = models.ImageField(upload_to='movies/images/', null=True, blank=True, default='movies/images/default2.jpg')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.title
