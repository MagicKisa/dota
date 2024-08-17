from utils import call_player_heroes, call_player_rank


class Player:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.rank = call_player_rank(link)
        self.heroes_info = call_player_heroes(link)

    def get_hero_info(self, hero_name):
        hero_info = self.heroes_info[hero_name]

        return hero_info
