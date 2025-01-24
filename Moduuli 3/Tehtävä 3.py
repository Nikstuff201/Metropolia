sukupuoli=input("Anna sukupuoli: ")
if sukupuoli != "mies" and sukupuoli != "nainen":
    print("virhe")
else:
    hemoglobiiniarvo=int(input("Anna hemoglobiiniarvo(g/l): "))
    if sukupuoli=="nainen":
        if hemoglobiiniarvo<117:
            print("hemoglobiiniarvo on alhainen")
        elif hemoglobiiniarvo>175:
            print("hemoglobiiniarvo on korkea")
        else:
            print("hemoglobiiniarvo on normaali")
    elif sukupuoli=="mies":
        if hemoglobiiniarvo<134:
            print("hemoglobiiniarvo on alhainen")
        elif hemoglobiiniarvo>195:
            print("hemoglobiiniarvo on korkea")
        else:
            print("hemoglobiiniarvo on normaali")
    else:
        print("Virhe")