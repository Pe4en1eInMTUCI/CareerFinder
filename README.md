
**_⚠️ Репозиторий собран из двух репозиториев:_**

[Backend](https://github.com/Pe4en1eInMTUCI/careerPractice)

[Frontend](https://github.com/Pe4en1eInMTUCI/careerWeb)

_p.s. Если нужна история коммитов их стоит искать там_

_p.s.s [Если уже хочется пощупать](https://github.com/Pe4en1eInMTUCI/CareerFinder?tab=readme-ov-file#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA) или [готовый веб](http://109.120.135.64:8080)_

# CareerFinder - сервис для поиска вакансий

### Сервис работает на базе API сайта hh.ru, есть возможность фильтра вакансий по графику и опыту работы.

### Так же можно уточнить поиск, например по городу, добаваив название города в поиск

Из дополнительного функционала:

При каждом выполненом поиске данные о параметрах запроса и том сколько было получено результатов записываются в БД

Информацию о самом популярном запросе и том сколько было найдено результатов можно посмотреть на странице /stats

---

### Более подробное описание прокта: 

## Проект поделен на два сервиса _CareerBackend_ и _CareerFrontend_. Каждый упакован в контейнер и запускается через docker compose

# CareerBackend

### Реализован через Flask, бд - SQlite, получал вакансии при помощи API hh.ru

Прописано три роута
- / корневой, ничего не делает
- /getVacancies GET, возвращает список вакансий по заданным параметрам
- /getMost GET, возвращает информацию о запросе с самым большим кол-вом вакансий

##### /getVacancies

Вызывает метод getVacancies из parser.py

Метод обращается к API hh.ru, получает 100 вакансий по заданным параметрам (название, график, опыт), формирует список только с необходимой информацией, и возвращает пользователю. Так же форматирует некоторые данные, например зарплаты

При каждом вызове метода записывает параметры запроса и количество найденых результатов в БД при помощи DataWorker.py метода createRecord()

##### /getMost

Вызывает метод getMost из DataWorker.py

Метод обращается к БД, и получает параметры запроса с самым большим кол-вом вакансий (пустые запросы не учитываются) и возвращает пользвателю

Перед запуском самого backend сервиса создается база данных vacancies.db, в ней создается таблица requests (если не были созданы ранее)

***


# CareerFrontend

### Реализован через Flask, обращается к бэку через библиотеку requests

Фронт написан без использования фреймворков, чистый html css запущенный через Flask

Прописано так же три роута
- / корневой, возвращает пользователю главную страницу
- /search возвращает пользователю страницу с вакансиями
- /stats возвращает информацию о запросе с самым большим кол-вом вакансий

#### Главная страница

На главной странице нет ничего кроме строки поиска и 5 слов

В поисковой строке можно указать, дополнительно город, график и опыт

<img width="1512" alt="1" src="https://github.com/Pe4en1eInMTUCI/CareerFinder/assets/62511045/b980fe48-e467-4a6f-908d-2026d6fea1f7">

_Плейсхолдер все время разный чтоб было красиво_

#### /search, она же страница с вакансиями

Сверху та же поисковая строка, снизу список вакансий

Список вакансии и поиск пользователя отображается при помощи jinja2

<img width="1512" alt="2" src="https://github.com/Pe4en1eInMTUCI/CareerFinder/assets/62511045/bef1f6e4-d560-4af3-9eb0-8ccd3cf0cce5">

Так же есть защита от кота на клавиатуре (когда в поле поиска рандомные символы или просто нет результатов)

<img width="1512" alt="3" src="https://github.com/Pe4en1eInMTUCI/CareerFinder/assets/62511045/e9031ab2-d834-4a61-9f6c-8a1865a5c33a">

Есть кнопка, которая откроет вакансию на hh.ru. Просто и лаконично

#### /stats, статистика

Просто страница где написан запрос с самым большим кол-вом вакансий, ничего более

***

# Запуск

```bash
sudo apt install git
sudo apt install docker
git clone https://github.com/Pe4en1eInMTUCI/CareerFinder.git
cd CareerFinder
docker compose up --build
```








