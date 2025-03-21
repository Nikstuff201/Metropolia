from random import randint

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=nopeus
        self.kuljettu_matka=kuljettu_matka

    def printall(self):
        print(f"{self.rekisteritunnus}  {self.huippunopeus}km/h   {self.nopeus}km/h   {self.kuljettu_matka}")

    def kiihdyttä(self,muutos):
        if self.nopeus+muutos>self.huippunopeus:
            self.nopeus=self.huippunopeus
        elif self.nopeus+muutos<0:
            self.nopeus=0
        else:
            self.nopeus+=muutos

    def kulje(self,tuntimäärä):
        self.kuljettu_matka=self.nopeus*tuntimäärä+self.kuljettu_matka

class Kilpailu:
    def __init__(self,nimi,pituus):
        self.nimi=nimi
        self.pituus=pituus
        self.autonlist=[]


    def tulosta_tilanne(self):
        for auto in self.autonlist:
            auto.printall()


    def kilpailu_ohi(self,auto):
        if auto.kuljettu_matka>=self.pituus:
            return True



    def tunti_kuluu(self):
        for auto in self.autonlist:
            auto.kiihdyttä(randint(-10, 15))
            auto.kulje(1)
            if self.kilpailu_ohi(auto)==True:
                return True








kilpailu1=Kilpailu("Suuri romuralli",8000)
for i in range(1,11):
    uusauto=Auto(f"ABC-{i}",randint(100,200))
    kilpailu1.autonlist.append(uusauto)

tunnit=1
kilpailuohi=False
while kilpailuohi!=True:
    kilpailuohi=kilpailu1.tunti_kuluu()
    if tunnit % 10 == 0:
        print("\n" + f"Tilanne {tunnit} tunnin jälkeen")
        kilpailu1.tulosta_tilanne()
    tunnit += 1


print("\n"+"peli on loppunut")
kilpailu1.tulosta_tilanne()

