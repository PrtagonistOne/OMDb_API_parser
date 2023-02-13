from django.contrib import admin
from episodes.models import Episode, Genre, Actor

# Register your models here.
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(Actor)
