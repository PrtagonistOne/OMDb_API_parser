import pytest

from episodes.models import Episode


@pytest.mark.django_db
def test_blog_create(episode_dummy_instances):
    #  given
    episode = episode_dummy_instances
    # when
    episode.save()
    # then
    assert Episode.objects.count() == 1
    assert isinstance(episode.imdbRating, float)
