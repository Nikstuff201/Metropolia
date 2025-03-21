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

autonlist=[]
for i in range(1,11):
    uusauto=Auto(f"ABC-{i}",randint(100,200))
    autonlist.append(uusauto)

race_finished=False
while not race_finished:
    for auto in autonlist:
        if auto.kuljettu_matka>=10000:
            race_finished=True
            break
        auto.kiihdyttä(randint(-10,15))
        auto.kulje(1)

for auto in autonlist:
    auto.printall()