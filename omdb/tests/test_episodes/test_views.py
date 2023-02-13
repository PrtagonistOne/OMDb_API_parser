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
    assert response.data == expected_results.data


@pytest.mark.django_db
def test_retrieve_episode(crud_APIFactory):
    # given
    episode_retrieve = EpisodeViewSet.as_view({'get': 'retrieve'})
    episode = Episode.objects.get(title='Winter Is Coming')
    expected_results = EpisodeSerializer(episode).data
    # when
    request = crud_APIFactory.get('/episodes/')
    response = episode_retrieve(request, pk=episode.pk)
    retrieved_post_data = response.data
    # then
    assert response.status_code == 200
    assert retrieved_post_data == expected_results


@pytest.mark.django_db
def test_filter_episode(crud_APIFactory):
    # given
    episode_list = EpisodeViewSet.as_view({'get': 'list'})
    # when
    filter_by_imdb_rating = Episode.objects.filter(imdb_rating__gt=8.8)
    filter_by_rating_title = Episode.objects.filter(imdb_rating__gt=8.8).filter(title__icontains='Is')
    filter_by_release_date = Episode.objects.filter(released__gt='2019-04-28')

    request_rating = crud_APIFactory.get('/episodes?imdb_rating=8.8')
    request_rating_title = crud_APIFactory.get('/episodes?imdb_rating=8.8&title=Is')
    request_released = crud_APIFactory.get('/episodes?released=2019-04-28')

    response_rating = episode_list(request_rating)
    response_rating_title = episode_list(request_rating_title)
    response_released = episode_list(request_released)
    # then
    assert response_rating.status_code == 200
    assert response_rating_title.status_code == 200
    assert response_released.status_code == 200

    assert len(response_rating.data) == len(filter_by_imdb_rating)
    assert len(response_rating_title.data) == len(filter_by_rating_title)
    assert len(response_released.data) == len(filter_by_release_date)

