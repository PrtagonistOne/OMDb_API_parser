import pytest

from episodes.models import Episode, Genre, Actor


@pytest.fixture()
def episode_dummy_instances():
    genre1 = Genre.objects.create(name='Action')
    genre2 = Genre.objects.create(name='Adventure')
    genre3 = Genre.objects.create(name='Drama')

    actor1 = Actor.objects.create(first_name='Sean', last_name='Bean')
    actor2 = Actor.objects.create(first_name='Mark', last_name='Addy')
    actor3 = Actor.objects.create(first_name='Nikolaj', last_name='Coster-Waldau')

    return Episode.objects.create(
        title='Winter Is Coming',
        released='2011-04-17',
        imdbRating=8.9,
        runtime='62 min',
        poster='https://m.media-amazon.com/images/M'
        '/MV5BMmVhODQ1NmUtMzJiYi00MGNiLWExNmQtYmUxNGJmY2U5ZmJlXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_SX300.jpg',
    )
