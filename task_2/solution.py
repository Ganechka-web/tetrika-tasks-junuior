import csv
from urllib import parse
from pprint import pprint

import requests 
from bs4 import BeautifulSoup, Tag


def find_next_page_link(html: str) -> str:
    pages_toolbar_id = 'mw-pages'

    parser = BeautifulSoup(html, 'html.parser')
    next_page_link = (
        parser.find('div', attrs={'id': pages_toolbar_id}) 
        .find('a', string='Следующая страница') 
        .attrs['href']
    )
    next_page_link = 'https://ru.wikipedia.org' + next_page_link

    return parse.unquote(next_page_link, encoding='utf-8')


def count_creatures_on_page(html: str) -> dict[str, int]:
    creatures: dict[str, int] = {}

    parser = BeautifulSoup(html, 'html.parser')
    creatures_tags: list[Tag] = (
        parser.find('div', attrs={'id': 'mw-pages'}) 
        .find('div', class_='mw-category mw-category-columns')
        .select('li a')
    )
    for tag in creatures_tags:
        creatures[tag.string[0]] = creatures.get(tag.string[0], 0) + 1

    return creatures


def merge_creatures_dicts(
    src: dict[str, int], other: dict[str: int]
) -> dict[str, int]:
    for key, value in other.items():
        src[key] = src.get(key, 0) + value

    return src


def get_creatures() -> dict[str, int]:
    next_page_link = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    creatures_by_alphabet: dict[str, int] = {}

    while 'A' not in creatures_by_alphabet:
        response = requests.get(next_page_link)
        creatures_by_alphabet = merge_creatures_dicts(
            creatures_by_alphabet, 
            count_creatures_on_page(response.text)
        )
        next_page_link = find_next_page_link(response.text)

    del creatures_by_alphabet['A'], creatures_by_alphabet['R']

    return creatures_by_alphabet


def fill_csv_counted_beasts():
    with open('beasts.csv', 'w', encoding='utf-8', newline='') as file:
        csv_writter = csv.writer(file)
        # write headers
        csv_writter.writerow(['letter', 'count'])

        creatures: dict[str, int] = get_creatures()
        for item in sorted(creatures.items(), key=lambda i: i[0].lower()):
            csv_writter.writerow(item)


if __name__ == '__main__':
    fill_csv_counted_beasts()
