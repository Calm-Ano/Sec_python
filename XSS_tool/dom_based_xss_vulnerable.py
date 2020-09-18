# coding: utf-8

from bottle import route
from bottle import run
from bottle import request
from bottle import response


@route('/')
def hello(user=''):
    user_name = request.query.get('user')
    user_name = '' if user_name is None else user_name

    # response.set_header('X-XSS-Protection', '1; mode=block')
    # response.set_header('Content-Security-Policy', 'default-src \'self\'')

    body = "<h2> Hello </h2>"
    script = "<Script>"
    script += "document.write(unescape('URL: ' + document.baseURI));"
    script += "</Script>"

    return body + script


run(host='0.0.0.0', port=8080, debug=True)
