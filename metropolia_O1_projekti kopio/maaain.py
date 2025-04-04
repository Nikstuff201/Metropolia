from Pelikauppa import pelikauppa
from Destination import destination
from projekti import combat,vaikeustaso
import copy
from Pelikauppa import pelikauppashowstats
from sql import scoreinsert
from sql import showscore


def vaikeustasoname(type):
    sanakirja={"small_airport":"easy",
    "medium_airport":"hard",
    "heliport":"medium",
    "large_airport":"insane"}
    return sanakirja[type]



class stats:
    def __init__(self, balance, maxhealth, health, damage, chance, name, score):
        self.balance = balance
        self.maxhealth = maxhealth
        self.health = health
        self.damage = damage
        self.chance = chance
        self.name = name
        self.score = score

playermin = stats(0, 3, 3, 1, 70, "player", 0)

strong_attack_helicopter = stats(0,1,1,2, 70, "Augusta Westland AH-1", 0)
strong_attack_helicopter0 = stats(0,1,1,2, 70, "Augusta Westland AH-1", 0)
attack_helicopter = stats(0,1,1,1, 60, "Denel Rooivalk", 0)
attack_helicopter1 = stats(0,1,1,1, 60, "Denel Rooivalk", 0)
attack_helicopter2 = stats(0,1,1,1, 60, "Denel Rooivalk", 0)
attack_helicopter3 = stats(0,1,1,1, 60, "Denel Rooivalk", 0)
scout_helicopter = stats(0,1,1,1, 40, "OH-58D", 0)
transport_helicopter = stats(0,2,2,1, 20, "Mi4MU", 0)

easy_enemy = stats(0,1,1,1, 50, "SPAD S.VII C.1", 0)
easy_enemy1 = stats(0,1,1,1, 50, "SPAD S.VII C.1", 0)
easy_enemy2 = stats(0,1,1,1, 50, "SPAD S.VII C.1", 0)

enemy = stats(0,2,2,1, 80, "Spitfire", 0)
enemy1 = stats(0,2,2,1, 80, "Spitfire", 0)
enemy2 = stats(0,2,2,1, 80, "Spitfire", 0)
enemy3 = stats(0,2,2,1, 80, "Spitfire", 0)
enemy4 = stats(0,2,2,1, 80, "Spitfire", 0)

bomber = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber0 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber1 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber2 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber3 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber4 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber5 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
bomber6 = stats(0,1,1,3, 40, "Avro Lancaster", 0)
stealth_bomber = stats(0,1,1,3, 70, "Northrop B-2 Spirit", 0)
stealth_bomber0 = stats(0,1,1,3, 70, "Northrop B-2 Spirit", 0)
stealth_bomber1 = stats(0,1,1,3, 70, "Northrop B-2 Spirit", 0)
boss = stats(0,3,3,2, 90, "USAF Lockheed Martin F-35A", 0)

fighter_jet = stats(0,2,2,2, 70, "Gloster Meteor", 0)
accurate_enemy = stats(0,1,1,1, 96, "A-10 Thunderbolt II", 0)
hard_enemy = stats(0,2,2,2, 80, "McDonnel F-15 Eagle", 0)
insane_enemy = stats(0,2,2,2, 85, "F/A-18C Hornet", 0)
resistant_enemy = stats(0,10,10,1, 60, "B-52 Stratofortress", 0)
kamikaze = stats(0,1,1,4, 50, "Mitsubishi Zero", 0)

easy1=(easy_enemy, easy_enemy1, easy_enemy2)
easy2=(easy_enemy, easy_enemy1, enemy)
easy3=(enemy,enemy1)
easy4=(easy_enemy,bomber)
medium1=(transport_helicopter,scout_helicopter)
medium2=(attack_helicopter,attack_helicopter2,strong_attack_helicopter)
medium3=(attack_helicopter,attack_helicopter1,attack_helicopter2,attack_helicopter3)
medium4=(strong_attack_helicopter,strong_attack_helicopter0)
hard1=(enemy,enemy1,enemy2,enemy3,enemy4)
hard2=(fighter_jet,hard_enemy)
hard3=(bomber,enemy,enemy2,easy_enemy)
hard4=(boss,)
insane1=(stealth_bomber,stealth_bomber0,stealth_bomber1)
insane2=(resistant_enemy,enemy,enemy1,enemy2,enemy3,enemy4)
insane3=(insane_enemy,hard_enemy,boss,accurate_enemy,fighter_jet)
insane4=(bomber,bomber0,bomber1,bomber2,bomber3,bomber4,bomber5,bomber6)
other=(kamikaze,kamikaze,kamikaze,kamikaze,accurate_enemy)


rowlength=61
choose=0
choose=""
while choose!="3":
    print("\n"+"*"*rowlength)
    print("What would you like to do".center(rowlength))
    print("1.Choose destination and start game".center(rowlength))
    print("2.Show score".center(rowlength))
    print("3.exit".center(rowlength))
    print("*"*rowlength+"\n")
    choose=str(input("Give your number(1,2,3):\n"))
    if choose=="1":
        player = copy.deepcopy(playermin)
        player.name = input("\nAnna player name:\n")
        while True:
            IATA=input("\n"+"Anna lentokentän IATA code, press R to choose random, write game difficulty level(easy,medium,hard,insane) to choose random airport by level or exit: \n")
            airport=destination(IATA.upper())
            if IATA.lower()=="exit":
                break
            elif airport==0:
                print("No such airport or variant")
            else:
                airportname=airport[0][0]
                airportregion=airport[0][1]
                airportmunicipality=airport[0][2]
                airporttype=airport[0][3]
                print("\n"+"*"*rowlength)
                print(airportname.center(rowlength))
                print(airportregion.center(rowlength))
                print(airportmunicipality.center(rowlength))
                print(airporttype.center(rowlength))
                print(f"Difficulty level: {vaikeustasoname(airporttype)}".center(rowlength))
                print("*"*rowlength+"\n")
                while True:
                    startgame=input("Start game?\n(Yes,Choose airport again, Shop or Exit)\n")
                    if startgame.lower()=="yes":
                        print("")
                        print("*"*rowlength)
                        pelikauppashowstats(player, rowlength)
                        print("*" * rowlength)
                        print("\n"+"*"*rowlength)
                        print(airportname.center(rowlength))
                        print(airportregion.center(rowlength))
                        print(airportmunicipality.center(rowlength))
                        print(airporttype.center(rowlength))
                        print(f"Difficulty level: {vaikeustasoname(airporttype)}".center(rowlength))
                        combat(player,copy.deepcopy(vaikeustaso(airporttype)))
                        print("*" * rowlength)
                        pelikauppashowstats(player,rowlength)
                        print("*" * rowlength+"\n")
                    elif startgame.lower()=="shop":
                        print("")
                        pelikauppa(player)
                        print("")
                    elif startgame.lower()=="choose airport again":
                        break
                    elif startgame.lower()=="exit":
                        break
                    else:
                        print("No such variant\n")
                if startgame.lower()=="exit":
                    break
        if player.score!=0:
            print("\n"+ "*" * rowlength)
            print(f"You score is {player.score}".center(rowlength))
            scoreinsert(player)
            showscore()
    elif choose=="2":
        print("")
        if showscore()==[]:
            print("*" * rowlength)
            print("No games played".center(rowlength))
            print("*"*rowlength)
    elif choose=="3":
        print("\n" + "*" * rowlength)
        print("Thank you for playing!".center(rowlength))
        print("*" * rowlength)
    else:
        print("No such variant")

