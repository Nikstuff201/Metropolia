class Auto:
    def __init__(self,rekisteritunnus,huippunopeus,tämänhetkinen_nopeus=0,kuljettu_matka=0):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.tämänhetkinen_nopeus=tämänhetkinen_nopeus
        self.kuljettu_matka=kuljettu_matka
    def printall(self):
        print(f"rekisteritunnus={self.rekisteritunnus}")
        print(f"huippunopeus={self.huippunopeus} km/h")
        print(f"tämänhetkinen nopeus={self.tämänhetkinen_nopeus} km/h")
        print(f"kuljettu matka={self.kuljettu_matka}")


uusi_auto=Auto("ABC-123",142)
uusi_auto.printall()