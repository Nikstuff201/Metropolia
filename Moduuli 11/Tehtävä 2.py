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


class Sähköauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti=akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self,rekisteritunnus,huippunopeus,bensatankin_koko):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensatankin_koko=bensatankin_koko


auto1=Sähköauto("ABC-15", 180, 52.5)
auto1.nopeus=100
auto2=Polttomoottoriauto("ACD-123", 165, 32.3)
auto2.nopeus=150

auto1.kulje(3)
print(auto1.kuljettu_matka)
auto2.kulje(3)
print(auto2.kuljettu_matka)

