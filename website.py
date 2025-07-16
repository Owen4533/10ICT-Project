from bottle import route, run, template, request
import requests
from datetime import datetime


@route('/<name>')
def index(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    response = response.json()
    age = response['age']
    return template('index', name=name, age=age)


@route('/')
def default():
    name = 'Owen'
    response = requests.get(f"https://api.agify.io/?name={name}")
    response = response.json()
    age = response['age']
    return template('index', name=name, age=age)


run(host='0.0.0.0', port=4000, reloader=True, debug=True)
