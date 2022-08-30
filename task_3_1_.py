# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет добавлять только новые вакансии/продукты в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты).
# То есть цифра вводится одна, а запрос проверяет оба поля

import sys
import pymongo
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint
from scrapper import VacancyScrapper as VS

_SEARCH_STR = 'планировщик'
_SALARY_MIN = 100000
_SALARY_CURRENCY = 'руб.'

def show_vacancies(salary_min, collection):
    result = collection.find({
        'salary_currency': {'$eq': _SALARY_CURRENCY},
        '$or': [{'salary_min': {'$gte': salary_min}}, {'salary_max': {'$gt': salary_min}}]
    })
    for item in result:
        pprint(item)

# def save_records(records, collection):
#     for record in records:
#         collection.update(record, record, upsert=True)

def save_records(records, collection):
    collection.insert_many(records)

def main():
    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancies20220801']
    analytics = db.analytics

    scrapper = VS(_SEARCH_STR)
    save_records(scrapper.storage, analytics)
    show_vacancies(_SALARY_MIN, analytics)

if __name__ == '__main__':
    sys.exit(main())


