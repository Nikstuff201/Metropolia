import mysql.connector
from flask import Flask

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='',
    password='',
    autocommit=True
)

app= Flask(__name__)
@app.route('/kenttä/<ICAO>')
def airport(ICAO):
    sql=f"SELECT name, municipality from airport where ident='{ICAO}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()

    vastaus={"ICAO":ICAO,
             "Name":f"{tulos[0][0]}",
             "Municipality":f"{tulos[0][1]}"}

    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)
