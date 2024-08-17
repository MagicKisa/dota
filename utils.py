import requests
import re
from bs4 import BeautifulSoup


class HeroInfo:
    def __init__(self, name, matches=0, winrate=0, kda=0):
        self.name = name
        self.matches = matches
        self.winrate = winrate
        self.kda = kda

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

pub_link = 'https://dotabuff.com'
esports_link = 'https://dotabuff.com/esports'


def call_player_heroes(player_link):    
    response = requests.get(player_link, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    
    tbody = soup.find('tbody')

    heroes_tr = tbody.find_all('tr')

    heroes_info = []
    for tr in heroes_tr:
        hero_name = tr.find('img')['alt']

        heroes_td = tr.find_all('td', class_="r-tab r-group-1")

        matches, winrate, kda = [td.text for td in heroes_td]

        hero_info = HeroInfo(hero_name, matches, winrate, kda)
        heroes_info.append(hero_info)

    return heroes_info

def call_player_rank(player_link):
    player_link = pub_link + player_link.split('esports')[-1].split('-')[0]
    
    response = requests.get(player_link, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    rank_div = soup.find('div', class_="leaderboard-rank-value")
    rank = rank_div.text

    return rank

def call_players_from_team(team_link):
    response = requests.get(team_link, headers=headers)
    
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    player_link_divs = soup.find_all('a', class_="esports-player esports-link player-link")


    player_links = []
    for div in player_link_divs:
       player_link = pub_link + div['href']

       if player_link not in player_links:
           player_links.append(player_link)

    return player_links
