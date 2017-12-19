import requests
import json

r=requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=Toulouse&apiKey=7a6f8095c87666e94af38a52189bdf19fd65ecfb")
data = r.json()
dataFiltrer=[]
for x in data:
    if x["available_bikes"] < 5:
        dataFiltrer.append(x)

print(json.dumps(dataFiltrer, indent = 4))



# API KEY = 7a6f8095c87666e94af38a52189bdf19fd65ecfb
