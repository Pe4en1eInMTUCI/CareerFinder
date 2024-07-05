
import requests
from currency_symbols import CurrencySymbols
import DataWorker

vacDefaultUrl = 'https://api.hh.ru/vacancies'

headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0"
}


def getVacancies(name, sch, exp):

    if sch == "None":
        params = {
            "text": name,
            "per_page": 100,
            "experience": exp
        }

        vacancies = requests.get(vacDefaultUrl, headers=headers, params=params)

        vacancies = vacancies.json()

        found = vacancies['found']

        items = vacancies['items']

        vacancies = []

        for item in items:

            if item['salary'] == None:
                salary = "Не указано"
            elif item['salary']['from'] == None:
                currency = str(item['salary']['currency'])
                if currency == "RUR":
                    currency = 'RUB'
                salary = "До " + str(item['salary']['to']) + str(CurrencySymbols.get_symbol(currency))
            elif item['salary']['to'] == None:
                currency = str(item['salary']['currency'])
                if currency == "RUR":
                    currency = 'RUB'
                salary = "От " + str(item['salary']['from']) + str(CurrencySymbols.get_symbol(currency))
            else:
                currency = str(item['salary']['currency'])
                if currency == "RUR":
                    currency = 'RUB'
                salary = "От " + str(item['salary']['from']) + str(CurrencySymbols.get_symbol(currency)) + " до " + str(item['salary']['to']) + str(CurrencySymbols.get_symbol(currency))

            requirement = str(item['snippet']['requirement'])

            if "highlighttext" in requirement:
                requirement = requirement.replace("<highlighttext>", "")
                requirement = requirement.replace("</highlighttext>", "")

            vacancy = {
                "name": item['name'],
                "area": item['area']['name'],
                "salary": salary,
                "url": item['alternate_url'],
                "requirement": requirement
            }

            vacancies.append(vacancy)

        DataWorker.createRecord(name, sch, exp, found)

        return vacancies

    params = {
        "text": name,
        "per_page": 100,
        "experience": exp,
        "schedule": sch
    }

    vacancies = requests.get(vacDefaultUrl, headers=headers, params=params)

    vacancies = vacancies.json()

    found = vacancies['found']

    items = vacancies['items']

    vacancies = []

    for item in items:

        if item['salary'] == None:
            salary = "Не указано"
        elif item['salary']['from'] == None:
            currency = str(item['salary']['currency'])
            if currency == "RUR":
                currency = 'RUB'
            salary = "До " + str(item['salary']['to']) + str(CurrencySymbols.get_symbol(currency))
        elif item['salary']['to'] == None:
            currency = str(item['salary']['currency'])
            if currency == "RUR":
                currency = 'RUB'
            salary = "От " + str(item['salary']['from']) + str(CurrencySymbols.get_symbol(currency))
        else:
            currency = str(item['salary']['currency'])
            if currency == "RUR":
                currency = 'RUB'
            salary = "От " + str(item['salary']['from']) + str(CurrencySymbols.get_symbol(currency)) + " до " + str(
                item['salary']['to']) + str(CurrencySymbols.get_symbol(currency))

        requirement = str(item['snippet']['requirement'])

        if "highlighttext" in requirement:
            requirement = requirement.replace("<highlighttext>", "")
            requirement = requirement.replace("</highlighttext>", "")

        vacancy = {
            "name": item['name'],
            "area": item['area']['name'],
            "salary": salary,
            "url": item['alternate_url'],
            "requirement": requirement
        }

        vacancies.append(vacancy)

    DataWorker.createRecord(name, sch, exp, found)

    return vacancies