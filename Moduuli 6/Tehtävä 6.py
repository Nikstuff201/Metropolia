def funktio (halkaisija,hinta):
    from math import pi
    pintaala=pi*(halkaisija/2)**2
    neliömetrihinta=hinta/pintaala*100**2
    return neliömetrihinta

halkaisija1=float(input("Anna pizza 1 halkaisija: "))
hinta1=float(input("Anna pizza 1 hinta: "))
halkaisija2=float(input("Anna pizza 2 halkaisija: "))
hinta2=float(input("Anna pizza 2 hinta: "))

if funktio(halkaisija1,hinta1)<funktio(halkaisija2,hinta2):
    print("Pizza 1 on edullisempi")
elif funktio(halkaisija1,hinta1)>funktio(halkaisija2,hinta2):
    print("Pizza 2 on edullisempi")
else:
    print("Nillä on sama arvo")




