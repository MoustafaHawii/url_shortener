import sqlite3

connection = sqlite3.connect('database.db')

c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS urls(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            original_url TEXT NOT NULL,
            clicks INTEGER NOT NULL DEFAULT 0
            )''')
