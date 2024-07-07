from flask import Flask, request
import parser
import DataWorker

app = Flask("main")

@app.route('/')
def root():
    return "200: OK!"


@app.route('/getVacancies')
def getVacancies():
    DataWorker.createTable()
    name = request.args.get('name')
    exp = request.args.get('experience')
    sch = request.args.get('schedule')

    return parser.getVacancies(name=name, exp=exp, sch=sch)

@app.route('/getStats')
def getStats():
    return DataWorker.getMost()


@app.route('/getAll')
def getAll():
    return DataWorker.getAll()



