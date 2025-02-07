lentoasemat={
"KLAX": "Los Angelesin kansainvälinen lentokenttä",
"EDDF": "Frankfurtin kansainvälinen lentokenttä",
"RJTT": "Tokion kansainvälinen lentokenttä (Haneda)"
}

while True:
    comand=input("Valitse komento (syöttää,hakea,lopettaa): ")
    if comand=="syöttää":
        koodi=input("Anna lentoaseman koodi: ")
        nimi=input("Anna lentoaseman nimi: ")
        lentoasemat[koodi]=nimi
    elif comand=="hakea":
        koodi=input("Anna lentoaseman koodi: ")
        if koodi in lentoasemat:
            print(lentoasemat[koodi])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif comand=="lopettaa":
        break
    else:
        print("Virheellinen komento, yritä uudelleen.")

print("lopetetaan toiminta")


