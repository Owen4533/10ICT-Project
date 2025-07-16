from bottle import route, run, template, view, static_file, request, redirect, error 
import requests
from datetime import datetime
@route('/')
def index():
 return template('index')

