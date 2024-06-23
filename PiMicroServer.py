import os
from bottle import route, run, static_file
@route('/')
def home():
  return
static_file('serverfile.html', root='.')

run(host='0.0.0.0', port=8080)
