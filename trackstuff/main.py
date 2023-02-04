from flask import Flask, render_template, request
from pickle import FALSE, TRUE
import datetime
import sqlite3
#################################################################################
app = Flask(__name__)
jahr = datetime.datetime.now()
aktuellesDatum = (jahr.strftime("%d.%m.%Y"))
aktuellesDatum2 = (jahr.strftime("%Y.%m.%d"))
#################################################################################
@app.route("/", methods = ["POST", "GET"])
def home():

    connect = sqlite3.connect('dokumentation.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM sport')
    sport = cursor.fetchall()
    cursor.execute('SELECT Datum FROM sport ORDER BY Datum DESC LIMIT 1')
    sport1 = cursor.fetchall()
    s = str(sport1)
    w = ("[('" + aktuellesDatum2 + "',)]")
    connect.commit()
    connect.close()
    icon = ""
    if s == w:
        icon = "icon1"

    Datum = request.form.get("Datum")
    Aktivität = request.form.get("Aktivität")
    Zeit = request.form.get("Zeit")

    if Datum != None and Aktivität != None and Zeit != None:
        connect = sqlite3.connect('dokumentation.db')
        cursor = connect.cursor()
        cursor.execute('insert into sport(Datum, Aktivität, Zeit)values(?,?,?)',(Datum, Aktivität, Zeit))
        connect.commit()
        connect.close()

    return render_template('home.html', aktuellesDatum=aktuellesDatum, sport=sport, icon=icon)
#################################################################################
if __name__ == '__main__':
    app.run(port=1910, debug=FALSE, threaded=FALSE)