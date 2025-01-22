leiviskät=float(input("Anna leiviskät:\n"))
naulat=float(input("\nAnna naulat:\n"))
luodit=float(input("\nAnna luodit:\n"))
summa=leiviskät*20*32*13.3+naulat*32*13.3+luodit*13.3
print("\nMassa nykymittojen mukaan:")
print(f"{int(summa//1000)} kilogrammaa ja {summa%1000:.2f} gramma")
