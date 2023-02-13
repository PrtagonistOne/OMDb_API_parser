import pytest
from episodes.serializers import EpisodeSerializer
from episodes.models import Episode, Genre, Actor

from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.renderers import JSONRenderer


@pytest.mark.django_db
def test_episode_serializer(dummy_db_instances):
    # given
    episode_serializer = EpisodeSerializer(Episode.objects.all(), many=True)
    # when
    content = JSONRenderer().render(episode_serializer.data)
    # then
    assert type(episode_serializer.data) == ReturnList
    assert type(content) == bytes
