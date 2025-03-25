class Julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi
    def tulosta_tiedot(self):
        print(self.nimi)

class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja=kirjoittaja
        self.sivumäärä=sivumäärä
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.kirjoittaja)
        print(self.sivumäärä)


class Lehti(Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja=päätoimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.päätoimittaja)

julkaisu1=Lehti("Aku Ankka","Aki Hyyppä")
julkaisu2=Kirja("Hytti no:6", "Rosa Liksom", 200)

julkaisu1.tulosta_tiedot()
print("")
julkaisu2.tulosta_tiedot()
