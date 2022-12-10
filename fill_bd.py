import sqlite3
from GetCardImg import getImg

conn = sqlite3.connect('database.db')

cur = conn.cursor()

with open('cards.txt') as f:
    lines = f.readlines()

for i in range(len(lines)//2):
    datas = lines[i*2].split()
    sep = datas.index(':')
    poke = " ".join(datas[:sep])
    etat = " ".join(datas[sep+1:])
    url = lines[i*2+1]
    img = getImg(url)
    print([poke, etat, url, img])
    cur.execute("INSERT INTO cards (name, status, link, img) VALUES (?, ?, ?, ?)",
    (poke, etat, url, img)
    )

conn.commit()
conn.close()
print("___________done___________")