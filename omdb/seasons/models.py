from django.db import models


class Season(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    season_number = models.IntegerField(blank=False, unique=False)
    total_seasons = models.IntegerField(blank=False, unique=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
