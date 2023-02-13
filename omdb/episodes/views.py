import os

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from episodes.models import Episode
from episodes.serializers import EpisodeSerializer


# Create your views here.
class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().prefetch_related('genre', 'actors')
    serializer_class = EpisodeSerializer

