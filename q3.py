import requests
import json
import sqlite3

conn = sqlite3.connect('anime.sqlite')
cursor = conn.cursor()

url = 'https://ghibliapi.herokuapp.com/films/'
r = requests.get(url)
print(r)
print(r.headers)
print(r.text)
res = r.json()
print(res)
print(json.dumps(res, indent=4))

with open('anime.json', 'w') as file:
    json.dump(res, file, indent=4)


print('My Neighbor Totoro გამოვიდა:', res[1]["release_date"], 'წელს')
print('Castle in the Sky გამოვიდა:', res[0]["release_date"], 'წელს')
print('My Neighbor Totoro_ს აღწერა:', res[0]["description"])
print('Castle in the Sky_ს აღწერა:', res[1]["description"])

list_rows = []
for each in res:
    title = each['title']
    producer = each['producer']
    release_date = each['release_date']
    running_time = each['running_time']
    row = (title, producer, release_date, running_time)
    list_rows.append(row)
print(list_rows)



cursor.execute('''CREATE TABLE IF NOT EXISTS StudioGhibli
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title INTEGER,
             producer INTEGER,
             release_date VARCHAR(50),
             running_time VARCHAR(50))
             ''')

cursor.executemany("INSERT INTO StudioGhibli(title, producer, release_date, running_time) VALUES (?, ?, ?, ?)", list_rows)



conn.commit()


