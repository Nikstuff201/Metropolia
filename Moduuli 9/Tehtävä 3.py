class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.nopeus=nopeus
        self.kuljettu_matka=kuljettu_matka

    def printall(self):
        print(f"rekisteritunnus={self.rekisteritunnus}")
        print(f"huippunopeus={self.huippunopeus} km/h")
        print(f"tämänhetkinen nopeus={self.nopeus} km/h")
        print(f"kuljettu matka={self.kuljettu_matka}")

    def kiihdyttä(self,muutos):
        if self.nopeus+muutos>self.huippunopeus:
            print(f"Nopeus ei voi olla enemmän kuin {self.huippunopeus}km/h")
            self.nopeus=self.huippunopeus
        elif self.nopeus+muutos<0:
            print(f"Nopeus ei voi olla vähemmän kuin 0 km/h")
            self.nopeus=0
        else:
            self.nopeus+=muutos

    def kulje(self,tuntimäärä):
        self.kuljettu_matka=self.nopeus*tuntimäärä+self.kuljettu_matka



uusi_auto=Auto("ABC-123",142)

uusi_auto.kuljettu_matka=2000
uusi_auto.nopeus=60
uusi_auto.kulje(float(input("Anna tunnin määrä: ")))
print(uusi_auto.kuljettu_matka)