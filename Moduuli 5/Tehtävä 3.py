luku=int(input("Anna luku: "))
if luku==0 or luku ==1:
    print("luku ei ole alkuluku")
else:
    for i in range(2,luku):
        if luku%i==0:
            print("luku ei ole alkuluku")
            break
    if i == luku-1:
        print("luku on alkuluku")

