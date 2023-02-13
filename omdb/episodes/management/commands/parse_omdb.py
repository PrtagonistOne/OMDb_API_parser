from django.core.management.base import BaseCommand
from django.core.management.color import no_style

from episodes.models import Episode, Genre, Actor
from django.db import connection
import requests
import json
import os
from parse import parse
import datetime


def clean_db_date() -> None:
    Episode.objects.all().delete()
    Genre.objects.all().delete()
    Actor.objects.all().delete()

    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Episode, Genre,
                                                                  Actor])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)


def genre_check(episode_json: dict, episode_obj: Episode) -> list:
    genres_check = [genre_c.get('name') for genre_c in Genre.objects.values()]
    genres = episode_json.get('Genre').split(', ')
    genres_instances = []
    if genres_check:
        genres_instances.extend(
            Genre.objects.create(name=genre, episode=episode_obj)
            for genre in genres
            if genre not in genres_check
        )
    else:
        genres_instances.extend(Genre.objects.create(name=genre, episode=episode_obj) for genre in genres)
    return genres_instances


def actor_check(episode_json: dict, episode_obj: Episode) -> list:
    actors_check = [actor_c.get('last_name') for actor_c in Actor.objects.values()]
    actors = episode_json.get('Actors').split(', ')
    actors_instances = []
    if actors_check:
        for actor in actors:
            first_name = actor.split(' ')[0]
            last_name = actor.split(' ')[1]
            if last_name in actors_check:
                continue
            actors_instances.append(Actor.objects.create(first_name=first_name, last_name=last_name,
                                                         episode=episode_obj))
    else:
        for actor in actors:
            first_name = actor.split(' ')[0]
            last_name = actor.split(' ')[1]

            actors_instances.append(Actor.objects.create(first_name=first_name, last_name=last_name,
                                                         episode=episode_obj))
    return actors_instances


def imdb_check(episode_json: dict) -> float or None:
    imdb_rating = episode_json.get('imdbRating')
    if imdb_rating == 'N/A':
        imdb_rating = None
    return imdb_rating


class Command(BaseCommand):
    help = 'Retrieve all of "Game of Throne" data from omdb and populate the database.'

    def handle(self, *args, **kwargs):
        clean_db_date()
        key = os.environ.get('OMDB_API_KEY')

        TOTAL_SEASONS = 8
        for season in range(TOTAL_SEASONS):
            omdb_by_episode = f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season + 1}&apikey={key}'
            page = requests.get(omdb_by_episode)
            season_json = json.loads(page.text)
            current_season_episodes = range(len(season_json['Episodes']))
            for episode in current_season_episodes:
                page_episode = requests.get(
                    f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season + 1}&episode={episode + 1}&apikey={key}')
                episode_json = json.loads(page_episode.text)
                date = parse('{y:d}-{m:d}-{d:d}', season_json['Episodes'][episode]['Released'])

                episode_obj = Episode.objects.create(
                    title=episode_json.get('Title'),
                    episode_number=episode_json.get('Episode'),
                    released=datetime.date(date['y'], date['m'], date['d']),
                    imdb_rating=imdb_check(episode_json),
                    runtime=episode_json.get('Runtime'),
                    poster=episode_json.get('Poster'),
                    season=season_json.get('Season')
                )
                actor_check(episode_json, episode_obj)
                genre_check(episode_json, episode_obj)
            self.stdout.write(f"Season#{season_json.get('Season')} was added")

