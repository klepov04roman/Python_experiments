raw = [
    {"name": "anna", "age": "29", "country": "PL", "score": "88"},
    {"name": "roman", "age": "30", "country": "UA", "score": "91"},
    {"name": "anna", "age": "29", "country": "PL", "score": "88"},  # дубликат
    {"name": "oleg", "age": "34", "country": "RU", "score": "56"},
    {"name": "daria", "age": "23", "country": "RU", "score": "73"},
]

# Словарь для замены стран
country_map = {
    "PL": "Poland",
    "UA": "Ukraine",
    "RU": "Ukraine"  # по примеру результата
}

# Удаление дубликатов (по всем ключам)
unique_raw = []
seen = set()

for entry in raw:
    # Создаём хэшируемое представление записи
    key = tuple(sorted(entry.items()))
    if key not in seen:
        seen.add(key)
        unique_raw.append(entry)

# Преобразование данных
for item in unique_raw:
    item["name"] = item["name"].capitalize()
    item["country"] = country_map.get(item["country"], item["country"])

# Результат
print(unique_raw)
