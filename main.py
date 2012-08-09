from bottle import route, run, error, post, request, redirect

messages = [['Jordan', 'hey, this is kinda cool']]

@route('/')
def index():
    my_output = '<p>Welcome to BottleChat!</p>'
    my_output += '<ul>'
    for message in messages:
        my_output += '<li>%s: %s</li>' % (message[0], message[1])
    my_output += '</ul>'

    my_output += '<form action="/message" method="post">'
    my_output += 'Name: <input type="text" name="name" /><br />'
    my_output += 'Message: <input type="text" name="message" /><br />'
    my_output += '<input type="submit" />'
    my_output += '</form>'

    return my_output

@post('/message')
def add_message():
    name = request.forms.name
    text = request.forms.message

    messages.append([name, text])
    redirect('/')

run(host='localhost', port=8080)
