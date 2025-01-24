import random
tietokoneenluku=random.randint(1,10)
käyttäjänluku=int(input("Anna luku: "))
while tietokoneenluku!=käyttäjänluku:
    if käyttäjänluku>tietokoneenluku:
        print("Liian suuri")
    elif käyttäjänluku<tietokoneenluku:
        print("Liian pieni")
    käyttäjänluku = int(input("Anna luku: "))
print("oikein")

