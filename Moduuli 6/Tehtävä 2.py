def funktio(tahkojenyhteismäärä):
    import random
    luku=random.randint(1,tahkojenyhteismäärä)
    return luku

tahkojenyhteismäärä=int(input("Anna tahkojen määrä: "))
i=0
while i != tahkojenyhteismäärä:
    tulos=funktio(tahkojenyhteismäärä)
    print(tulos)
    i=tulos


