from django.core.management.base import BaseCommand
# from seasons.models import Season
# from episodes.models import Episode, Genre, Actor

import requests
import json


class Command(BaseCommand):
    help = 'Retrieve all of "Game of Throne" data from omdb and populate the database.'

    def handle(self, *args, **kwargs):
        key = 'e321e8d1'
        for season in range(8):
            omdb_by_episode = f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season + 1}&apikey={key}'
            page = requests.get(omdb_by_episode)
            season_json = json.loads(page.text)
            self.stdout.write(season_json['Title'])
            exit()
            for episode in range(len(season_json['Episodes'])):
                page_episode = requests.get(
                    f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season + 1}&episode={episode + 1}&apikey={key}')
                get_json = json.loads(page_episode.text)
                print(get_json)
