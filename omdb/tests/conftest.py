import pytest

from episodes.models import Episode, Genre, Actor
from rest_framework.test import APIRequestFactory


@pytest.fixture()
def dummy_db_instances() -> None:
    episode = Episode.objects.create(
        title='Winter Is Coming',
        episode_number=1,
        released='2011-04-17',
        imdb_rating=8.9,
        runtime='62 min',
        poster='https://m.media-amazon.com/images/M'
        '/MV5BMmVhODQ1NmUtMzJiYi00MGNiLWExNmQtYmUxNGJmY2U5ZmJlXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_SX300.jpg',
    )

    Genre.objects.create(name='Action')
    Genre.objects.create(name='Adventure')
    Genre.objects.create(name='Drama')

    Actor.objects.create(first_name='Sean', last_name='Bean')
    Actor.objects.create(first_name='Mark', last_name='Addy')
    Actor.objects.create(first_name='Nikolaj', last_name='Coster-Waldau')


@pytest.fixture()
def crud_APIFactory(dummy_db_instances):
    return APIRequestFactory()
