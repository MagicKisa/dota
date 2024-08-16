import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def call_player_info(player_link):
    pass

def call_player_rank(player_link):
    response = requests.get(player_link, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find('div', class_="leaderboard-rank-value")
    rank = div.text

    return rank


    
