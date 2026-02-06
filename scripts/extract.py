import requests 
import json

#API URL 
LAUNCHES_URL = "https://api.spacexdata.com/v4/launches"
ROCKETS_URL = "https://api.spacexdata.com/v4/rockets"


#Получаем данные
launches = requests.get(LAUNCHES_URL).json()
rockets = requests.get(ROCKETS_URL).json()


#Сохраняем в JSON
with open("data/launches.json", "w") as f:
	json.dump(launches, f, indent=2)

with open("data/rockets.json", "w") as f:
	json.dump(rockets, f, indent=2)
