import mysql.connector
def lentokentojenlukumäärä(iso_country):
    sql1=f"SELECT type, COUNT(*) as 'total' from airport WHERE iso_country='{iso_country}' GROUP BY type"
    kursori=yhteys.cursor()
    kursori.execute(sql1)
    tulos=kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(f"{rivi[0]}={rivi[1]}")
    return

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='nikstuff',
    password='Nekich54510',
    autocommit=True
)

koodi=input("Anna maan koodi: ")
lentokentojenlukumäärä(koodi)


            
