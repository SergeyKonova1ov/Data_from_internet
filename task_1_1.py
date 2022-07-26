# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
from pprint import pprint



url = 'https://api.github.com'
user = 'SergeyKonova1ov'

response = requests.get(f'{url}/users/{user}/repos')

if response.ok:# если код ошибки меньше 400, то продолжаем
    pass

j_data = response.json()

for i in j_data:

    pprint(i['name'])

