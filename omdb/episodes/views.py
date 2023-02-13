from rest_framework import viewsets, filters

from episodes.filters import EpisodeFilter
from episodes.models import Episode
from episodes.serializers import EpisodeSerializer


# Create your views here.
class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.prefetch_related('genre', 'actors').all()
    serializer_class = EpisodeSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       EpisodeFilter)
    search_fields = ('title', 'episode_number', 'imdb_rating', 'season')
    ordering_fields = ('id', 'imdb_rating', 'released')
    ordering = ('id',)

