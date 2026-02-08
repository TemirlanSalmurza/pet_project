import json
import os

def transform_data():
    
    os.makedirs("data", exist_ok=True)

    # Загружаем данные из extract
    try:
        with open("data/launches.json") as f:
            launches = json.load(f)
        with open("data/rockets.json") as f:
            rockets = json.load(f)
    except FileNotFoundError:
        print("Файлы launches.json или rockets.json не найдены")
        return

    # Пример трансформации:
    # Берём только нужные поля и связываем с ракетами
    rocket_dict = {r['id']: r['name'] for r in rockets}

    transformed_launches = []
    for launch in launches:
        transformed_launches.append({
            "name": launch.get("name"),
            "date_utc": launch.get("date_utc"),
            "rocket": rocket_dict.get(launch.get("rocket"), "Unknown"),
            "success": launch.get("success")
        })

    # Сохраняем трансформированные данные
    with open("data/transformed_launches.json", "w") as f:
        json.dump(transformed_launches, f, indent=2)

    print(f"Трансформация завершена: {len(transformed_launches)} записей"
