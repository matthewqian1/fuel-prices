import sqlite3

con = sqlite3.connect('../data.db')

cur = con.cursor()

cur.execute('SELECT * FROM postcodes_geo limit 1')

print(cur.fetchone())
