from django.db import models

# Create your models here.
class Film(models.Model):
    title   = models.CharField(max_length=120)
    year    = models.IntegerField()
    imgUrl  = models.CharField(max_length=120)
