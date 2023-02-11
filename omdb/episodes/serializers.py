from .models import Episode, Genre, Actor

from rest_framework import serializers


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['title', 'released', 'imdb_rating', 'runtime', 'poster',
                  'season', 'genre', 'actors']
        depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']
