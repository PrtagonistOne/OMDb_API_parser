import pytest

from episodes.models import Episode, Genre, Actor


@pytest.mark.django_db
def test_episode_create(dummy_db_instances):
    #  given
    episode = Episode.objects.get(title='Winter Is Coming')
    # when
    episode.save()
    # then
    assert Episode.objects.count() == 1
    assert isinstance(episode.imdb_rating, float)


@pytest.mark.django_db
def test_genre_create(dummy_db_instances):
    # given
    # when
    episode = Episode.objects.get(title='Winter Is Coming')
    action_genre = Genre.objects.all().get(name='Action')
    adventure_genre = Genre.objects.all().get(name='Adventure')
    drama_genre = Genre.objects.all().get(name='Drama')
    # then
    assert episode.genre_set.get(name="Action").name == action_genre.name
    assert episode.genre_set.get(name="Adventure").name == adventure_genre.name
    assert episode.genre_set.get(name="Drama").name == drama_genre.name


@pytest.mark.django_db
def test_actors_create(dummy_db_instances):
    # given
    # when
    episode = Episode.objects.get(title='Winter Is Coming')
    actor1 = Actor.objects.get(last_name='Bean')
    actor2 = Actor.objects.get(last_name='Addy')
    actor3 = Actor.objects.get(last_name='Coster-Waldau')
    # then
    assert episode.actor_set.get(last_name='Bean').first_name == actor1.first_name
    assert episode.actor_set.get(last_name='Addy').first_name == actor2.first_name
    assert episode.actor_set.get(last_name='Coster-Waldau').first_name == actor3.first_name
