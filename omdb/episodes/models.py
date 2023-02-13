from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    episode_number = models.IntegerField(null=True, unique=False)
    released = models.DateField(blank=False, unique=False)
    imdb_rating = models.FloatField(null=True, unique=False)
    runtime = models.CharField(max_length=10, unique=False, blank=False)
    poster = models.CharField(max_length=500, unique=True, blank=False)
    season = models.IntegerField(null=True, unique=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
