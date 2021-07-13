import sqlite3
import re

conn = sqlite3.connect('counting_org.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)')

archive = input('Introduce archive name:')
if len(archive) < 1: fhandler = open('mbox.txt')
else:
    fhandler = open(archive)

for line in fhandler:
    if not line.startswith('From:'): continue
    else:
        email = re.findall('^From:.+?@(.+)\s', line)
        email = str(email[0])

        cur.execute('SELECT org FROM Counts WHERE org = ?', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (email,))
conn.commit()
cur.close()
