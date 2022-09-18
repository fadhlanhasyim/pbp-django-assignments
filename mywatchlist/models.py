from django.db import models

# Create your models here.
class MywatchlistModel(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField()
    release_date = models.DateField()
    review = models.TextField()
