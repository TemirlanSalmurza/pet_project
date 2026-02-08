import json
import csv
import os

def load_data():
    
    os.makedirs("data", exist_ok=True)

    # Загружаем трансформированные данные
    try:
        with open("data/transformed_launches.json") as f:
            transformed_launches = json.load(f)
    except FileNotFoundError:
        print("Файл transformed_launches.json не найден")
        return

    # Сохраняем данные в CSV (пример "загрузка")
    csv_file = "data/final_launches.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "date_utc", "rocket", "success"])
        writer.writeheader()
        for row in transformed_launches:
            writer.writerow(row)

    print(f"Данные загружены в {csv_file}, всего записей: {len(transformed_launches)}")
