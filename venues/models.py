from django.contrib.gis.db import models
from django.contrib.auth.models import User


# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    openingHours = models.CharField(max_length=100)
    venueType = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.venue.name}"