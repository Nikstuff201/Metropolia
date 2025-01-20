leiviskät=float(input("Anna leiviskät:\n"))
naulat=float(input("Anna naulat:\n"))
luodit=float(input("Anna luodit:\n"))
summa=leiviskät*20*32*13.3+naulat*32*13.3+luodit*13.3
print("Massa nykymittojen mukaan:")
print(f"{summa//1000} kilogrammaa ja {summa%1000:.2f} gramma")
