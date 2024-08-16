from utils import call_hero_info

class HeroInfo:
    def __init__(self, name, matches=0, winrate=0, kda=0):
        self.name = name
        self.matches = matches
        self.winrate = winrate
        self.kda = kda

class Player:
    def __init__(self, name, link, rank=None, heroes_info=[]):
        self.name = name
        self.link = link
        self.rank = rank
        self.heroes_info = heroes_info

    def get_hero_info(self, hero_name, profile="esports"):
        player_link = self.link
        hero_info = call_hero_info(player_link, hero_name, profile)

        return hero_info
