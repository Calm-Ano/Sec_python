# coding: utf-8

from bottle import route, request, run, template


@route('/hello')
def index(user=''):
    username = request.query.get('user')
    return template('<h1>Hello {{ user }}', user=username)


run(host='0.0.0.0', port=8080)
