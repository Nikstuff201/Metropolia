import requests
import json
apikey=input("Anna apikey: ")
paikkakunta=input("Anna paikkakunnan nimi: ")
pyyntö=f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta},&APPID={apikey}"

vastaus=requests.get(pyyntö).json()
print(vastaus["weather"][0]["description"]+f", {vastaus["main"]["temp"]-273.15:.2f} ℃")