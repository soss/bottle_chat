from bottle import route, run

@route('/:name')
def index(name):
    return '<b>Hello, %s!</b>' % name

run(host='localhost', port=8080)
