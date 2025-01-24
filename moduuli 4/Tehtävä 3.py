luku=input("Anna luku: ")
luvut=[]
while luku != "":
    luvut.append(float(luku))
    luku = input("Anna luku: ")
if len(luvut)<2:
    print("virhe")
else:
    print(f"pienimmän luku on {min(luvut)} ja suurimman luku on {max(luvut)}")
