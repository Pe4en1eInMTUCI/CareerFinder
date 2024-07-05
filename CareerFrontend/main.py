import requests
from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def root():

    jobs = ['Программист', 'Врач', 'Учитель', 'Архитектор', 'Юрист', 'Менеджер', 'Инженер', 'Дизайнер', 'Маркетолог', 'Повар']
    cities = ['Москва', 'Минск', 'Кишинев', 'СПб', 'Ереван', 'Астана', 'Алматы', 'Баку']
    randomJob = random.choice(jobs)
    randomCity = random.choice(cities)

    return render_template('index.html', randomJob=randomJob, randomCity=randomCity)


@app.route('/search')
def search():
    job = request.args.get("job")
    sch = request.args.get("schedule")
    exp = request.args.get("experience")

    data = requests.get(f"http://127.0.0.1:8800/getVacancies?name={job}&experience={exp}&schedule={sch}").json()

    return render_template('search.html', job=job, vacancies=data)

@app.route('/stats')
def stats():

    data = requests.get("http://127.0.0.1:8800/getStats").json()


    return render_template('stats.html', request=data[0], count=data[1])

if __name__ == '__main__':
    app.run(debug=True, port=1020)