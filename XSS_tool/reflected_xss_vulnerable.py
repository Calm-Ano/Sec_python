# coding: utf-8

from bottle import route
from bottle import run
from bottle import request
import html


@route('/')
def hello(user=''):
    user_name = request.query.get('user')
    user_name = '' if user_name is None else user_name
    user_name = html.escape(user_name)

    body = "<h2> Hello {name} </h2>".format(name=user_name)

    return body


run(host='0.0.0.0', port=8080, debug=False)
