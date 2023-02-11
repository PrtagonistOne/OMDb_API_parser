import pytest
from episodes.serializers import EpisodeSerializer, ActorSerializer, GenreSerializer
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


@pytest.mark.django_db
def test_genre_serializer(dummy_db_instances):
    # given
    genre_serializer = GenreSerializer(Genre.objects.all(), many=True)
    # when
    content = JSONRenderer().render(genre_serializer.data)
    # then
    assert type(genre_serializer.data) == ReturnList
    assert type(content) == bytes


@pytest.mark.django_db
def test_actor_serializer(dummy_db_instances):
    # given
    actor_serializer = ActorSerializer(Actor.objects.all(), many=True)
    # when
    content = JSONRenderer().render(actor_serializer.data)
    # then
    assert type(actor_serializer.data) == ReturnList
    assert type(content) == bytes
