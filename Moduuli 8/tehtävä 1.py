import mysql.connector

def airportsijainti (ICAO):
    sql=f"SELECT name, municipality FROM airport WHERE ident='{ICAO}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(f"Airport name is {rivi[0]}")
            print(f"Airport place is {rivi[1]}")
    else:
        print("not airport found")
    return


yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='nikstuff',
    password='Nekich54510',
    autocommit=True
)

icao=input("Anna ICAO koodi: ")
airportsijainti(icao)



