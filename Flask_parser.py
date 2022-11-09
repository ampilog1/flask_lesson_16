import requests
from bs4 import BeautifulSoup
import pprint


def parce():
    # Будем получать данные с сайта ГЭС-2. Поскольку на сайте ничего не понятно, сделаем карту сайта
    url = 'https://v-a-c.org/ges2'

    response = requests.get(url)  # получаем данные с сайта
    print(response.status_code)
    # pprint.pprint(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')  # делаем из них суп

    map_site = {}  # создаем словарь для карты сайта
    links = soup.find_all('a')  # извлекаем  все теги со ссылками
    # pprint.pprint(links)

    for link in links:  # для всех элементов получившегося объекта извлекаем название и ссылку
        text = link.text
        href = link.get('href')
        map_site[text] = href  # делаем из них словарь
    return map_site