import sqlite3
import datetime
jahr = datetime.datetime.now()
aktuellesDatum = (jahr.strftime("%Y.%m.%d"))
#
Datum = "0000.00.00"
#Datum = aktuellesDatum

Aktivität = "Muster"
Zeit = 1
#
connect = sqlite3.connect('dokumentation.db')
#
cursor = connect.cursor()
#
#Tabellen erstellen
connect.execute('create table if not exists sport (Datum timestamp, Aktivität text, Zeit integer)')
cursor.execute('insert into sport(Datum, Aktivität, Zeit)values(?,?,?)',(Datum, Aktivität, Zeit))
cursor.execute('SELECT * FROM sport')
#
#cursor.execute('DROP TABLE sport')
#
a = cursor.fetchall()
print(a)
#
connect.commit()
connect.close()