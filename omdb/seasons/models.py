from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.last_name


class Episode(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    released = models.DateField(blank=False, unique=False)
    imdbRating = models.FloatField(blank=False, unique=False)
    runtime = models.CharField(max_length=10, unique=False, blank=False)
    poster = models.CharField(max_length=500, unique=True, blank=False)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title