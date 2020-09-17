# coding: utf-8

from bottle import route
from bottle import run
from bottle import request
from bottle import redirect
import sqlite3


db_name = 'tasklist.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


@route('/')
def hello(user=''):
    tasks = get_tasklist()

    body = "<h2>Persistent XSS Demo</h2>"
    body += "<form action='./' method='POST'>"
    body += "タスク名: <input type='text' name='name' /><br>"
    body += "内容: <input type='text' name='detail' /><br>"
    body += "<input type='submit' name='register' value='登録' />"
    body += "</form>"
    body += tasks

    return body


@route('/', method='POST')
def register():
    name = request.forms.get('name')
    detail = request.forms.get('detail')

    sql_query = 'INSERT INTO tasklist values(?, ?)'
    cursor.execute(sql_query, (name, detail))
    conn.commit()

    return redirect('/')


def get_tasklist():
    sql_query = 'SELECT * FROM tasklist'
    result = cursor.execute(sql_query)

    body = '<table border="1">'
    for row in result:
        body += '<tr><td>'
        body += row[0].encode(encoding="utf-8", errors="strict")
        body += '</td><td>'
        body += row[1].encode(encoding="utf-8", errors="strict")
        body += '</td><tr>'

    body += '</table>'
    return body


run(host='0.0.0.0', port=8080, debug=True)
