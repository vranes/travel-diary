from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    cost = models.IntegerField(default=0)
    travel_agency = models.CharField(max_length=100)
    num_travellers = models.IntegerField(default=0)

    def __str__(self):
        return self.content

    def is_popular(self):
        return self.num_travellers > 5


class Entry(models.Model):
    date = models.DateField(null=True)
    content = models.TextField()
    traveller = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
