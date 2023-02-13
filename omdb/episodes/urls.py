from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from episodes.views import EpisodeViewSet

episode_list = EpisodeViewSet.as_view({
    'get': 'list',
})
episode_detail = EpisodeViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('episodes/', episode_list, name='episode-list'),
    path('episodes/<int:pk>/', episode_detail, name='episode-detail'),
])
