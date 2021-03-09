import sqlite3

db = sqlite3.connect("database.db")

db.execute("CREATE TABLE skills (name TAXT, progress integer, user_id integer)")