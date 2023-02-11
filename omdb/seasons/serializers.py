from .models import Season

from rest_framework import serializers


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['title', 'season_number', 'total_seasons']
        depth = 1

