#!/usr/bin/env python

from bottle import route, run, template
import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()

@route('/')
def index():
    c.execute('SELECT * FROM movie ORDER BY RANDOM() LIMIT 1;')
    movie_id, title, year, director_id = c.fetchone()
    director = c.execute('SELECT name FROM director WHERE id={}'.format(director_id)).fetchone()[-1]
    
    return '{} - "{}" directed by {} {}'.format(year, title, director, '<p onClick="window.location.reload()"> Next </p> <style>body{background:#111;color:#fff;font-size:13px;text-align:center;padding-top:300px;}</style>')

run(host='localhost', port=8080)
