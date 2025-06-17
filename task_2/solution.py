import csv
from urllib import parse

import requests 
from bs4 import BeautifulSoup, Tag


def get_next_page_link(html: str) -> str:
    """Rerurns found the next page link with protocol and host"""
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
    """Ruturs counted creatures on the html page"""
    creatures: dict[str, int] = {}

    parser = BeautifulSoup(html, 'html.parser')
    # get all links with creatures titles
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
    """Returns all counted beasts on ru.wikipedia.org"""
    next_page_link = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    creatures_by_alphabet: dict[str, int] = {}

    # Untill first latin letter on the page (russian alphabet is over)
    while 'A' not in creatures_by_alphabet:
        response = requests.get(next_page_link)
        creatures_by_alphabet = merge_creatures_dicts(
            creatures_by_alphabet, 
            count_creatures_on_page(response.text)
        )
        next_page_link = get_next_page_link(response.text)

    del creatures_by_alphabet['A'], creatures_by_alphabet['R']

    return creatures_by_alphabet


def fill_csv_counted_beasts():
    """Fill beasts.csv file sorted and counted beasts"""
    creatures: dict[str, int] = get_creatures()
    creatures_on_write: tuple[str, int] = sorted(
        creatures.items(), key=lambda i: i[0].lower()
    ) 

    with open('beasts.csv', 'w', encoding='utf-8', newline='') as file:
        csv_writter = csv.writer(file)
        # write headers
        csv_writter.writerow(['letter', 'count'])

        # write all creatures rows
        csv_writter.writerows(creatures_on_write)


if __name__ == '__main__':
    fill_csv_counted_beasts()
