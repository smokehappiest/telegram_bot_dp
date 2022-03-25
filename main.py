from bs4 import BeautifulSoup
from items import item_list
import requests
import re


class Hero:
    def __init__(self, hero_name: str, winrate: float, matches: int, wins: int, hero_href: str):
        self.hero_name = hero_name
        self.winrate = winrate
        self.matches = matches
        self.wins = wins
        self.losses = matches - wins
        self.hero_href = hero_href

    def show_Hero_stats(self, pos=0):
        if (pos != 0):
            return str(self.hero_name + ' ' + f'{self.winrate}% ' + self.matches)
        return str(self.hero_name + ' ' + f'{self.winrate}% ' + str(self.matches))

    def get_Hero_url(self, pos=0):
        return (self.hero_href)


url = 'https://www.dota2protracker.com'
response = requests.get(url + '/meta')
soup = BeautifulSoup(response.text, 'html.parser')


def get_list_heroes(type: int, soup):
    meta_all = soup.find("div", class_='meta-scenario', id=f"tabs-{type}")
    heroes = meta_all.find("div", class_='meta-picks')
    a = heroes.find_all('a', href=True)

    all_heroes = []
    for item in a:
        hero_name = item.find('div', class_='meta-pick-title').text
        hero_stats = item.find_all('div', class_='meta-pick-info-block')
        meta_hero_statistic = {}
        hero_href = item.get('href')
        for stat in hero_stats:
            value = stat.text
            if (('winrate') in value):
                meta_hero_statistic['winrate'] = (
                    ''.join(liter for liter in value if (liter.isdigit()) or liter == '.'))
            elif (('matches') in value):
                meta_hero_statistic['matches'] = ''.join(liter for liter in value if (liter.isdigit()) or liter == '.')
            elif (('wins') in value):
                meta_hero_statistic['wins'] = ''.join(liter for liter in value if (liter.isdigit()) or liter == '.')
        all_heroes.append(Hero(hero_name, float(meta_hero_statistic['winrate']), int(meta_hero_statistic['matches']),
                               int(meta_hero_statistic['wins']), hero_href))
    return all_heroes


def show_buy(all_heroes, pos=0):
    pass


def get_buy_list(hero_url):
    response = requests.get(url + hero_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    buy_all = soup.find('div', id="all_roles")
    role_box = buy_all.find('div', class_='role_box', id="role_Offlane")  #### ROLE!!!!!!!!!
    items_box = role_box.find_all('div', class_='role_box_items')
    for item in items_box:
        items = item.find_all('div', class_='role-inventory-item')
        for x in items:
            textx = x.get('title')
            print(textx)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    return


def show_statistic(all_heroes, pos=0):
    output=''
    if (pos != 0):
        return str(all_heroes[pos - 1].get_Hero_url())
    for x in range(0, len(all_heroes)):
        output += all_heroes[x].show_Hero_stats() + '\n'
    return output


all_heroes = get_list_heroes(4, soup)
"""
while (True):
    operation = input()
    if (operation == 'show'):
        show_statistic(all_heroes)
    elif (operation.startswith('buy ')):
        get_buy_list(all_heroes[int(operation[3:]) - 1].get_Hero_url())
"""