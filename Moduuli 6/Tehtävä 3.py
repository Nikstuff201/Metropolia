def bensiininmäärä (nestegallona):
    return (nestegallona*3.785)

gallona=float(input("Anna nestegallonoja: "))
while gallona>=0:
    print (f"{bensiininmäärä (gallona)} litraa")
    gallona = float(input("Anna nestegallonoja: "))