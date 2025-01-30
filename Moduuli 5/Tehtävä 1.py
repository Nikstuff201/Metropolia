import random
määrä=int(input("Arpakuutioiden lukumäärä: "))
summa=0
for _ in range(määrä):
    summa+=random.randint(1,6)
print(f"summa={summa}")