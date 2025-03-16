import mysql.connector

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='',
    password='',
    autocommit=True
)

kursori = yhteys.cursor()
kursori.execute("CREATE TABLE IF NOT EXISTS Score (id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255) NOT NULL, SCORE INT NOT NULL)")

def scoreinsert(player):
    sql="INSERT INTO SCORE(NAME,SCORE) VALUES(%s, %s)"
    kursori=yhteys.cursor()
    kursori.execute(sql, (player.name, player.score))
    yhteys.commit()

def showscore():
    sql="SELECT NAME,SCORE FROM SCORE ORDER BY SCORE DESC LIMIT 10"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    rowlength=61
    x=1
    if tulos==[]:
        return tulos
    else:
        for player, score in tulos:
            print("*" * rowlength)
            print(f"{x}".center(rowlength))
            print(f"{player}:{score}".center(rowlength))
            x += 1
        print("*" * rowlength)


