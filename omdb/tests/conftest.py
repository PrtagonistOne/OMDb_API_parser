import pytest

from episodes.models import Episode, Genre, Actor


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

    Genre.objects.create(name='Action', episode=episode)
    Genre.objects.create(name='Adventure', episode=episode)
    Genre.objects.create(name='Drama', episode=episode)

    Actor.objects.create(first_name='Sean', last_name='Bean', episode=episode)
    Actor.objects.create(first_name='Mark', last_name='Addy', episode=episode)
    Actor.objects.create(first_name='Nikolaj', last_name='Coster-Waldau', episode=episode)
