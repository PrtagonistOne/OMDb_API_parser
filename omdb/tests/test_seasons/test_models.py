import pytest

from seasons.models import Season


@pytest.mark.django_db
def test_season_model(dummy_db_instances):
    # given
    season = Season.objects.get(title="Game of Thrones")
    new_season_title = 'Game of Pytest'
    # when
    season.title = new_season_title
    season.save()
    # then
    assert season.title == new_season_title
    assert isinstance(season.season_number, int)
