import requests
import string
from bs4 import BeautifulSoup


def remove_punctuation(value):
    result = ""
    for c in value:
        if c not in string.punctuation:
            result += c
    return result


req = requests.get('http://www.7english.ru/dictionary.php?id=3500&letter=all')
root = BeautifulSoup(req.content, 'html.parser')
en_ru = []
for tr in root.select('tr'):
    if 'onmouseover' not in tr.attrs:
        continue
    td_list = [td.text.strip() for td in tr.select('td')]
    if len(td_list) != 9 or not td_list[1] or not td_list[5]:
        continue
    en = td_list[1]
    ru = td_list[5].split(', ')[0]
    en_ru.append((en, ru))
    en_ru.append(('my', 'мой'))
    en_ru.append(('you', 'ты'))
    en_ru.append(('is', 'есть'))
    en_ru.append(('i', 'я'))
    en_ru.append(('what', 'что'))
    en_ru.append(('are', ''))

# word_dict = dict(en_ru)
# print(len(en_ru), en_ru)
# for ddd in en_ru: print(en_ru[ddd])
# print(users_dict)
# print(users_dict[ddd])
