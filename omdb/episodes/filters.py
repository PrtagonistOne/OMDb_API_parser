from rest_framework.filters import BaseFilterBackend

from episodes.models import Episode


class EpisodeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        query_params = request.query_params

        for query_param in query_params:
            if query_param == 'title':
                queryset = queryset.filter(title__icontains=query_params.get('title'))
            elif query_param == 'episode_number':
                queryset = queryset.filter(episode_number=query_params.get('episode_number'))
            elif query_param == 'released':
                queryset = queryset.filter(released__gt=query_params.get('released'))
            elif query_param == 'imdb_rating':
                queryset = queryset.filter(imdb_rating__gt=query_params.get('imdb_rating'))
            elif query_param == 'season':
                queryset = queryset.filter(season=query_params.get('season'))

        return queryset
