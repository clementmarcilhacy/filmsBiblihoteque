from django.db import models
from django.urls import reverse

# Create your models here.
class Film(models.Model):
    title   = models.CharField(max_length=120)
    year    = models.IntegerField()
    imgUrl  = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("films:film-details", kwargs={"my_id": self.id}) #f"/films/{self.id}/"
