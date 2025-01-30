list=[]
luku=input("Anna luku: ")
while luku != "":
    list.append(int(luku))
    luku=input("Anna luku: ")
list.sort(reverse=True)
print(list[0:5])