# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию через curl, Postman, Python.
# Ответ сервера записать в файл (приложить скриншот для Postman и curl)
import json
from typing import TextIO

import requests
from pprint import pprint

#chrome://version/
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'X-Yandex-API-Key': 'dacd0d35-7387-4bc0-890b-526baa712fc8'}
params = {'lat': '55.833333',
          'lon': '37.616667',
          'lang': 'ru_RU'
          }

url = 'https://api.weather.yandex.ru/v2/forecast' # тестовый тариф

response = requests.get(url, headers=headers, params=params )
j_data = response.json()
pprint(j_data)

with open('j_data', 'w') as f:
    json.dump(j_data, f)

