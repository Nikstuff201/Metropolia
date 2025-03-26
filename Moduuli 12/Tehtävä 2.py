import requests
import json

paikkakunta=input("Anna paikkakunnan nimi: ")
pyyntö=f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta},&APPID=0dfcd980a5b0bc8c920c471163b44469"

vastaus=requests.get(pyyntö).json()
print(vastaus["weather"][0]["description"]+f", {vastaus["main"]["temp"]-273.15:.2f} ℃")