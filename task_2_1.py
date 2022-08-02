# Необходимо собрать информацию о вакансиях на вводимую должность
# (используем input или через аргументы получаем должность) с сайтов HH(обязательно) и/или Superjob(по желанию).
# Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
from task_2_1_def import salaryinfo


params = {
    'area': '1',
    'search_field': 'name',
    'search_field': 'company_name',
    'search_field': 'description',
    'text': 'spider',
    'clusters': 'true',
    'ored_clusters': 'true',
    'enable_snippets': 'true',
    'page': '0',
    'hhtmFrom': 'vacancy_search_list'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

url = 'https://hh.ru/search/vacancy'

session = requests.session()
response = session.get(url, params=params, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')
vacancyes = dom.find_all('div',{'class': 'vacancy-serp-item__layout'})  # блоки вакансий - все тэги 'div' с указанным классом.

# vacancy_list = dom.select('a.bloko-link') # другой вариант- все тэги 'а' у которых есть класс bloko-link

# pprint(vacancyes)
#

last_page = dom.find('a', {'class': 'bloko-button', 'data-qa': 'pager-page'}).text

vacancyes_list = []

for i in range(0, int(last_page) +1):
    params = {
        'area': '1',
        'search_field': 'name',
        'search_field': 'company_name',
        'search_field': 'description',
        'text': 'spider',
        'clusters': 'true',
        'ored_clusters': 'true',
        'enable_snippets': 'true',
        'page': 'i',                      # переменный номер страницы
        'hhtmFrom': 'vacancy_search_list'
    }

    response = session.get(url, params=params, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    vacancyes = dom.find_all('div', {'class': 'vacancy-serp-item__layout'})

    for vacancy in vacancyes:
        vacancy_data = {}
        name = vacancy.find('a', {'class': 'bloko-link'})
        href = name.get('href')
        name = name.text
        salarytext = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
        vacancy_data['name'] = name
        vacancy_data['href'] = href
        vacancy_data['salary'] = salaryinfo(salarytext)

        vacancyes_list.append(vacancy_data)

pprint(vacancyes_list)

# with open('vacancyes.json','w') as vcn:
#     json.dump(vacancyes_list,vcn)
#     pd.read_json('vacancyes.json')
