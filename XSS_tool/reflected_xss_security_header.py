# coding: utf-8

from bottle import route
from bottle import run
from bottle import request
from bottle import response


@route('/')
def hello(user=''):
    user_name = request.query.get('user')
    user_name = '' if user_name is None else user_name

    response.set_header('X-XSS-Protection', '1; mode=block')
    response.set_header('Content-Security-Policy', 'default-src \'self\'')
    html = '<h2> Hello {name} </h2>'.format(name=user_name)

    return html


run(host='0.0.0.0', port=8080, debug=True)
