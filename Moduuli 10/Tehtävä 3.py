class Hissi:
    def __init__(self,nykyinen_kerros,alimman_kerros=1,ylimmän_kerros=10):
        self.nykyinen_kerros=nykyinen_kerros
        self.alimman_kerros=alimman_kerros
        self.ylimmän_kerros=ylimmän_kerros


    def kerros_ylös(self,kerros):
        for i in range(kerros-self.nykyinen_kerros):
            self.nykyinen_kerros+=1
            print(f"Hissi on nyt {self.nykyinen_kerros} kerroksella")

    def kerros_alas(self,kerros):
       for i in range(self.nykyinen_kerros-kerros):
            self.nykyinen_kerros-=1
            print(f"Hissi on nyt {self.nykyinen_kerros} kerroksella")

    def siirry_kerrokseen(self,numero):
        if numero>self.ylimmän_kerros or numero<self.alimman_kerros:
            print("Ei ole tätä kerosta")
        else:
            if numero>self.nykyinen_kerros:
                self.kerros_ylös(numero)
            elif numero<self.nykyinen_kerros:
                self.kerros_alas(numero)
            else:
                print("Sinä olet samalla kerroksella")


class Talo:
    def __init__(self,alimman_kerros,ylimmän_kerros,hissien_lukumäärä):
        self.alimman_kerros=alimman_kerros
        self.ylimmän_kerros=ylimmän_kerros
        self.hissien_lukumäärä=hissien_lukumäärä
        self.hissit=[]

    def aja_hissiä(self,hissnum,kerros):
            hissi=self.hissit[hissnum-1]
            hissi.siirry_kerrokseen(kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alimman_kerros)


alimman_kerros=int(input("Anna talon alemman kerros: "))
ylimmän_kerros=int(input("Anna talon ylimmän kerros: "))
hissien_lukumäärä=int(input("Anna talon hissien lukumäärä: "))
talo=Talo(alimman_kerros,ylimmän_kerros,hissien_lukumäärä)
for i in range(talo.hissien_lukumäärä):
    hissi = Hissi(nykyinen_kerros=alimman_kerros,alimman_kerros=talo.alimman_kerros,ylimmän_kerros=talo.ylimmän_kerros)
    talo.hissit.append(hissi)
hissnum=4
if 1<=hissnum<=len(talo.hissit):
    talo.aja_hissiä(hissnum,9)
else:
    print("Ei ole tätä hissiä")

talo.palohälytys()