import mysql.connector
yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='',
    password='',
    autocommit=True
)

def destination(IATA):
    sanakirja = {"easy": "small_airport",
                 "hard": "medium_airport",
                 "medium": "heliport",
                 "insane": "large_airport"}
    import random
    type=""
    if IATA=="R":
        while True:
            id=random.randint(1,70942)
            sql = f"SELECT name, iso_country as 'countrys abbreviation',municipality, type FROM airport WHERE id={id}"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            if tulos!=[]:
                type=tulos[0][3]
                if type not in ("closed", "seaplane_base", None, ""):
                    break
    elif IATA.lower()=="easy" or IATA.lower()=="medium" or IATA.lower()=="hard" or IATA.lower()=="insane":
        sql = f"SELECT name, iso_country as 'countrys abbreviation',municipality, type FROM airport WHERE type='{sanakirja[IATA.lower()]}' ORDER BY RAND() LIMIT 1"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
    else:
        tarkistus=f"SELECT COUNT(*) FROM airport WHERE iata_code='{IATA}'"
        kursori=yhteys.cursor()
        kursori.execute(tarkistus)
        tulos=kursori.fetchall()
        if 0 in tulos[0]:
            tulos=0
            return tulos
        else:
            sql=f"SELECT name, iso_country as 'countrys abbreviation',municipality, type FROM airport WHERE iata_code ='{IATA.upper()}' and type!='seaplane_basez' and type!='closed'"
            kursori=yhteys.cursor()
            kursori.execute(sql)
            tulos=kursori.fetchall()
    return tulos











