class Hissi:
    def __init__(self,nykyinen_kerros=1,alimman_kerros=1,ylimmän_kerros=10):
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

hissi=Hissi()
while True:
    kerros=int(input("Anna kerroksen numero: "))
    if kerros==20:
        break
    hissi.siirry_kerrokseen(kerros)