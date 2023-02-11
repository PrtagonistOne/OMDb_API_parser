import requests
import json

key = 'e321e8d1'
for season in range(8):
    omdb_by_episode = f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season+1}&apikey={key}'
    page = requests.get(omdb_by_episode)
    season_json = json.loads(page.text)
    print(season_json)
    for episode in range(len(season_json['Episodes'])):
        page_episode = requests.get(f'http://www.omdbapi.com/?t=Game%20of%20Thrones&season={season+1}&episode={episode+1}&apikey={key}')
        get_json = json.loads(page_episode.text)
        print(get_json)
