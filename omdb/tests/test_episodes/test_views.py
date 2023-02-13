import pytest

from episodes.models import Episode
from episodes.serializers import EpisodeSerializer
from episodes.views import EpisodeViewSet


@pytest.mark.django_db
def test_list_episode(crud_APIFactory):
    # given
    episode_list = EpisodeViewSet.as_view({'get': 'list'})
    expected_results = EpisodeSerializer(Episode.objects.all(), many=True)
    # when
    request = crud_APIFactory.get('/episodes/')
    response = episode_list(request)
    # then
    assert response.status_code == 200
    assert response.data['results'] == expected_results.data


@pytest.mark.django_db
def test_retrieve_retrieve(crud_APIFactory):
    # given
    episode_retrieve = EpisodeViewSet.as_view({'get': 'retrieve'})
    episode = Episode.objects.get(pk=1)
    expected_results = EpisodeSerializer(episode).data
    # when
    request = crud_APIFactory.get('/episodes/')

    response = episode_retrieve(request, pk=1)
    retrieved_post_data = response.data
    # then
    assert response.status_code == 200
    assert retrieved_post_data == expected_results
