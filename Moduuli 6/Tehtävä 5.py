def funktio(lista):
    uuslist=[]
    for i in lista:
        if i%2==0:
            uuslist.append(i)
    return uuslist

lista=[1,2,3,4,5,6,7,8,9,10]
uuslist=funktio(lista)
print(uuslist)
