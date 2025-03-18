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



uusi_auto=Auto("ABC-123",142)

while True:
    muutos=int(input("Anna nopeuden muutos(km/h): "))
    uusi_auto.kiihdyttä(muutos)
    print(f"nykyinen nopeus {uusi_auto.nopeus} km/h")