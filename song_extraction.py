import requests 
from bs4 import BeautifulSoup
import re

def extract_top_100songs_by_date(date):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    if not pattern.match(date):
        return 'not a valid date'
    billboard_top_100_url= f'https://www.billboard.com/charts/hot-100/{date}'
    response= requests.get(billboard_top_100_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # get list of titles
    tags_list_of_songs= soup.select('li ul li h3')
    song_names= [tag.getText().strip() for tag in tags_list_of_songs]
    

    return song_names

print(extract_top_100songs_by_date('1999-02-09'))
    