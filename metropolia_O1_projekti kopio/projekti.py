import random

class stats:
    def __init__(self, balance, maxhealth, health, damage, chance, name, score):
        self.balance = balance
        self.maxhealth = maxhealth
        self.health = health
        self.damage = damage
        self.chance = chance
        self.name = name
        self.score = score

player = stats(0, 3, 3, 1, 70, "player", 0)

strong_attack_helicopter = stats(50,1,1,2, 70, "Augusta Westland AH-1", 50)
strong_attack_helicopter0 = stats(50,1,1,2, 70, "Augusta Westland AH-1", 50)
attack_helicopter = stats(25,1,1,1, 60, "Denel Rooivalk", 25)
attack_helicopter1 = stats(25,1,1,1, 60, "Denel Rooivalk", 25)
attack_helicopter2 = stats(25,1,1,1, 60, "Denel Rooivalk", 25)
attack_helicopter3 = stats(25,1,1,1, 60, "Denel Rooivalk", 25)
scout_helicopter = stats(10,1,1,1, 40, "OH-58D", 10)
transport_helicopter = stats(10,2,2,1, 20, "Mi4MU", 10)

easy_enemy = stats(15,1,1,1, 50, "SPAD S.VII C.1", 15)
easy_enemy1 = stats(15,1,1,1, 50, "SPAD S.VII C.1", 15)
easy_enemy2 = stats(15,1,1,1, 50, "SPAD S.VII C.1", 15)

enemy = stats(30,2,2,1, 80, "Spitfire", 30)
enemy1 = stats(30,2,2,1, 80, "Spitfire", 30)
enemy2 = stats(30,2,2,1, 80, "Spitfire", 30)
enemy3 = stats(30,2,2,1, 80, "Spitfire", 30)
enemy4 = stats(30,2,2,1, 80, "Spitfire", 30)

bomber = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber0 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber1 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber2 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber3 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber4 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber5 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
bomber6 = stats(40,1,1,3, 40, "Avro Lancaster", 40)
stealth_bomber = stats(60,1,1,3, 70, "Northrop B-2 Spirit", 60)
stealth_bomber0 = stats(60,1,1,3, 70, "Northrop B-2 Spirit", 60)
stealth_bomber1 = stats(60,1,1,3, 70, "Northrop B-2 Spirit", 60)
boss = stats(100,3,3,2, 90, "USAF Lockheed Martin F-35A", 100)

fighter_jet = stats(60,2,2,2, 70, "Gloster Meteor", 60)
accurate_enemy = stats(55,1,1,1, 96, "A-10 Thunderbolt II", 55)
hard_enemy = stats(65,2,2,2, 80, "McDonnel F-15 Eagle", 65)
insane_enemy = stats(70,2,2,2, 85, "F/A-18C Hornet", 70)
resistant_enemy = stats(90,10,10,1, 60, "B-52 Stratofortress", 90)
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

def attack(damage,chance):
    hit = random.randint(0,100)
    hit+=chance-70
    if hit<=30:
        return 0
    else:
        return damage

def bullying():
    message=random.randint(1,5)
    if message==1:
        print(""*61)
        print("You died".center(61))
        print("" * 61)
    elif message==2:
        print("" * 61)
        print("get good".center(61))
        print("" * 61)
    elif message==3:
        print("" * 61)
        print("gg".center(61))
        print("" * 61)
    elif message==4:
        print("" * 61)
        print("ez".center(61))
        print("" * 61)
    elif message==5:
        print("" * 61)
        print("skill issue".center(61))
        print("" * 61)

def combat(player, enemies):
    player.health = player.maxhealth
    while player.health>0:
        counter=0
        print("*"*61)
        for i, enemy in enumerate(enemies):
            if enemy.health>0:
                print(f"[{i+1}] {enemy.name} - HP:{enemy.health}/{enemy.maxhealth}, ATK:{enemy.damage}, Accuracy:{enemy.chance}%".center(61))
                counter+=1
        if counter == 0:
            print("Victory".center(61))
            if enemies == easy1 or easy2 or easy3 or easy4 or other:
                player.balance+=100
                player.score+=100
            elif enemies == medium1 or medium2 or medium3 or medium4:
                player.balance += 200
                player.score += 200
            elif enemies == hard1 or hard2 or hard3 or hard4:
                player.balance += 400
                player.score += 400
            elif enemies == insane1 or insane2 or insane3 or insane4:
                player.balance += 600
                player.score += 600
            return player
        print("*"*61)
        choice = int(input("Choose an enemy to attack (enter number): "))-1
        if 0 <= choice < len(enemies) and enemies[choice].health > 0:
            damage_dealt = attack(player.damage, player.chance)
            if damage_dealt != 0:
                enemies[choice].health -= damage_dealt
                if enemies[choice].health>0:
                    print("Target Hit".center(61))
                else:
                    print("Target Down".center(61))
                    player.balance += enemies[choice].balance
                    player.score += enemies[choice].score
            else:
                print("Miss".center(61))
        else:
            print("Target not found".center(61))
            continue
        print("*"*61)
        if any(enemy.health>0 for enemy in enemies):
            for enemy in enemies:
                if enemy.health>0:
                    damage_taken=attack(enemy.damage, enemy.chance)
                    if damage_taken!=0:
                        player.health-=damage_taken
                        if damage_taken>0:
                            print(f"{enemy.name} shot you for {damage_taken} damage".center(61))
                            print(f"hp:{player.health}/{player.maxhealth}".center(61))
                    else:
                        print(f"{enemy.name} missed".center(61))
        print(f"Balance: {player.balance}".center(61))
        print(f"Score: {player.score}".center(61))
        if player.health <= 0:
            bullying()
            return player

def vaikeustaso(type):
    if type=="small_airport":
        C=random.randint(1,4)
        if C == 1:
            return easy1
        elif C == 2:
            return easy2
        elif C == 3:
            return easy3
        else:
            return easy4
    elif type=="heliport":
        C = random.randint(1, 4)
        if C == 1:
            return medium1
        elif C == 2:
            return medium2
        elif C == 3:
            return medium3
        else:
            return medium4
    elif type=="medium_airport":
        C = random.randint(1, 4)
        if C == 1:
            return hard1
        elif C == 2:
            return hard2
        elif C == 3:
            return hard3
        else:
            return hard4
    elif type == "large_airport":
        C = random.randint(1, 4)
        if C == 1:
            return insane1
        elif C == 2:
            return insane2
        elif C == 3:
            return insane3
        else:
            return insane4
    else:
        return other

def start_combat(iata_code):
    global player
    difficulty = vaikeustaso(iata_code)
    player = combat(player, difficulty)

if __name__ == "__main__":
    combat(player, other)
