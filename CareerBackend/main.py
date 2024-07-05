
from flask import Flask, request
import parser
import DataWorker

app = Flask(__name__)

@app.route('/')
def root():
    return "200: OK!"


@app.route('/getVacancies')
def getVacancies():
    name = request.args.get('name')
    exp = request.args.get('experience')
    sch = request.args.get('schedule')

    return parser.getVacancies(name=name, exp=exp, sch=sch)

@app.route('/getStats')
def getStats():
    return DataWorker.getMost()

if __name__ == '__main__':
    DataWorker.createTable()
    app.run(debug=True, port=1034)
