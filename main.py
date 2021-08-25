import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Example (Name TEXT, Age REAL, Sport TEXT)')

name = "Kai"
age = 21
sport = "swim"

def data_entry(name, age, sport):
    c.execute("INSERT INTO Example (Name, Age, Sport) VALUES(?, ?, ?)",(name, age, sport))

    conn.commit()

create_table()
data_entry(name, age, sport)

c.close()
conn.close()