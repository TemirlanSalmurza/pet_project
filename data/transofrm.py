import json 
import pandas as pd


--------------- Launches

#Загружаем raw JSON
with open("data/launches.json") as f:
	launches_raw = json.load(f)


#Преобразуем в DataFrame
launches_df = pd.json_normalize(launches_raw)


#Выбираем нужные поля 

launches_stg = launches_df[[
    "id", "name", "date_utc", "rocket", "success", "flight_number"
]]

#Преобразуем дату 

launches_stg["date_utc"] = pd.to_datetime(launches_stg["date_utc"])

#Сохраняем как CSV
launches_stg.to_csv("data/launches_stg.csv", index=False)

---------------------- Rockets

with open("data/rockets.json") as f:
	rockets_raw = json.load(f)

rockets_df = pd.json_normalize(rockets_raw)
rockets_stg = rockets_df[[
    "id", "name", "first_flight", "country"
]]

rockets_stg.to_csv("data/rockets_stg.csv", index=False)
