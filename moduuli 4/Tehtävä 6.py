import random
N=int(input("Pisteiden määrä: "))
n=0
for i in range(N):
    piste=(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0))
    if piste[0]**2+piste[1]**2<1:
        n+=1
pi=4*(n/N)
print(pi)




