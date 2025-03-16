def pelikauppashowstats(player, rowlength):
    print("YOUR STATS".center(rowlength))
    print(f"balance={player.balance}$".center(rowlength))
    print(f"maxhealth={player.maxhealth}".center(rowlength))
    print(f"damage={player.damage}".center(rowlength))
    print(f"hit chance={player.chance}%".center(rowlength))
    print(f"score={player.score}".center(rowlength))





def pelikauppa(player):
    #STATS
    rowlength = 61
    print("*"*rowlength)
    pelikauppashowstats(player,rowlength)
    #HEALTH INCREASE
    healthnumber=1
    healthprice=100
    healthboost=1
    print ("*"*rowlength)
    print(f"{healthnumber}".center(rowlength))
    print("MAXHEALTH INCREASE".center(rowlength))
    print(f"(Increases maxhealth by {healthboost} point)".center(rowlength))
    print(f"Price {healthprice}$".center(rowlength))
    #DAMAGE INCREASE
    damagenumber=2
    damageprice=100
    damageboost=1
    print ("*"*rowlength)
    print(f"{damagenumber}".center(rowlength))
    print("DAMAGE INCREASE".center(rowlength))
    print(f"(Increases damage by {damageboost} point)".center(rowlength))
    print(f"Price {damageprice}$".center(rowlength))
    #CHANCE INCREASE
    chancenumber=3
    chanceprice=100
    chanceboost=2
    print("*" * rowlength)
    print(f"{chancenumber}".center(rowlength))
    print("CHANCE INCREASE".center(rowlength))
    print(f"(Increases hit chance by {chanceboost}%)".center(rowlength))
    print(f"Price {chanceprice}$".center(rowlength))
    print("*" * rowlength+"\n")

    choice=str(input(f"Give the number of your choice\n({healthnumber},{damagenumber},{chancenumber} or exit): "))
    while choice != "exit":
        if choice==f"{healthnumber}":
            if player.balance>=healthprice:
                player.maxhealth+=healthboost
                print (f"Maxhealth increased by {healthboost}")
                print (f"Your maxhealth now is {player.maxhealth}")
                player.balance-=healthprice
                print (f"Your balance now is {player.balance}\n")
            else:
                print("Not enough money!\n")
        elif choice==f"{damagenumber}":
            if player.balance>=damageprice:
                player.damage+=damageboost
                print (f"Damage increased by {damageboost}")
                print (f"Your damage now is {player.damage}")
                player.balance-=damageprice
                print (f"Your balance now is {player.balance}$\n")
            else:
                print("Not enough money!\n")
        elif choice==f"{chancenumber}":
            if player.chance<100:
                if player.balance>=chanceprice:
                    player.chance+=2
                    print (f"Chance increased by {chanceboost}%")
                    print(f"Your hit chance now is {player.chance}%")
                    player.balance-=chanceprice
                    print (f"Your balance now is {player.balance}$\n")
                else:
                    print("Not enough money!\n")
            else:
                print("Your hitchance now is maximum!\n")
        else:
            print("Command not found\n")
        choice=str(input(f"Give the number of your choice\n({healthnumber},{damagenumber},{chancenumber} or exit): "))

    print("\n"+"*"*rowlength)
    pelikauppashowstats(player, rowlength)
    print("*"*rowlength)
    return player








