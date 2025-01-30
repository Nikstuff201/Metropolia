käyttäjätunnus="python"
salasana="rules"
käyttäjänk=input("Anna käyttäjätunnus: ")
salasanak=input("Anna salasana: ")
kerrat=1
while kerrat <5:
    kerrat += 1
    if käyttäjätunnus != käyttäjänk or salasana != salasanak:
        käyttäjänk = input("Anna käyttäjätunnus: ")
        salasanak = input("Anna salasana: ")
    else:
        break
if käyttäjätunnus==käyttäjänk and salasana==salasanak:
    print("Tervetuloa")
else:
    print("Pääsy evätty")