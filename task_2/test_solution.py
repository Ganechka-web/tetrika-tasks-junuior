import csv

from task_2.solution import fill_csv_counted_beasts


def test_fill_csv_counted_beasts():
    fill_csv_counted_beasts()

    with open('beasts.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        counted_beasts = {}
        for letter, count in csv_reader:
            counted_beasts[letter] = count
        
        assert len(counted_beasts) - 1 == 30
        assert int(counted_beasts['А']) == 1301
        assert int(counted_beasts['Я']) == 228
