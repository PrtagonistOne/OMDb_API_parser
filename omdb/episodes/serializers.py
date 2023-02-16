from .models import Episode, Genre, Actor

from rest_framework import serializers


class EpisodeSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Episode
        fields = [
            "title",
            "released",
            "imdb_rating",
            "runtime",
            "poster",
            "genre",
            "actors",
        ]
