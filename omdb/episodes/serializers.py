from .models import Episode, Genre, Actor

from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']


class EpisodeSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='last_name'
    )

    class Meta:
        model = Episode
        fields = ['title', 'released', 'imdb_rating', 'runtime', 'poster', 'genre', 'actors']
        depth = 1
