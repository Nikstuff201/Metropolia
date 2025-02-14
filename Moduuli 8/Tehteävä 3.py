import mysql.connector
from geopy.distance import geodesic

def etäisyys(icao1, icao2):
    sql=f"SELECT latitude_deg, longitude_deg FROM airport where ident='{icao1}' or ident='{icao2}' group by ident"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount==2:
        point1=(tulos[0][0],tulos[0][1])
        point2=(tulos[1][0],tulos[1][1])
        distance=geodesic(point1,point2).kilometers
    print(f"Etäisyys lentokentojen välillä on {distance} kilometria")

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='nikstuff',
    password='Nekich54510',
    autocommit=True
)

icao1=input("Anna ensimmäisen lentokennan koodi: ")
icao2=input("Anna toisen lentokennan koodi: ")
etäisyys(icao1,icao2)
