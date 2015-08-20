#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('movies.db')
c = conn.cursor()
c.execute('SELECT * FROM movie ORDER BY RANDOM() LIMIT 1;')
movie_id, title, year, director_id = c.fetchone()
director = c.execute('SELECT name FROM director WHERE id={}'.format(director_id)).fetchone()[-1]
    
print('{} - "{}" directed by {}'.format(year, title, director))
